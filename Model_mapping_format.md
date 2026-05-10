 1. What model name does the client send?                                                                                         
                                                                                                                                   
  The client sends a Claude model id, not the upstream NIM name. The proxy classifies that name and remaps it.                     
                                                                                                                                     Routing logic lives in config/settings.py::Settings.resolve_model (and api/model_router.py):                                     
                                                                                                                                     name_lower = claude_model_name.lower()                                                                                         
  if "opus"   in name_lower and self.model_opus   is not None: return self.model_opus
  if "haiku"  in name_lower and self.model_haiku  is not None: return self.model_haiku
  if "sonnet" in name_lower and self.model_sonnet is not None: return self.model_sonnet
  return self.model

  So with your .env:

  ┌─────────────────────────────────────────────────────┬─────────────────┬─────────────────────────────────────────────┐
  │              Client sends model field               │ Substring match │             Routed to upstream              │
  ├─────────────────────────────────────────────────────┼─────────────────┼─────────────────────────────────────────────┤
  │ claude-opus-4-20250514                              │ opus            │ NIM model deepseek-ai/deepseek-v4-pro       │
  ├─────────────────────────────────────────────────────┼─────────────────┼─────────────────────────────────────────────┤
  │ claude-sonnet-4-20250514 (or claude-3-5-sonnet-...) │ sonnet          │ NIM model z-ai/glm-5.1                      │
  ├─────────────────────────────────────────────────────┼─────────────────┼─────────────────────────────────────────────┤
  │ claude-haiku-4-20250514 (or claude-3-5-haiku-...)   │ haiku           │ NIM model moonshotai/kimi-k2.5              │
  ├─────────────────────────────────────────────────────┼─────────────────┼─────────────────────────────────────────────┤
  │ something-else (no opus/sonnet/haiku substring)     │ none            │ Fallback MODEL → NIM minimaxai/minimax-m2.7 │
  └─────────────────────────────────────────────────────┴─────────────────┴─────────────────────────────────────────────┘

  The list of advertised ids is in api/routes.py::SUPPORTED_CLAUDE_MODELS. Pick any of them — e.g. claude-sonnet-4-20250514.

  The provider prefix (nvidia_nim/) is stripped server-side; only the part after the first / is forwarded to NVIDIA NIM as the
  OpenAI-style model field (see Settings.parse_model_name and providers/nvidia_nim/request.py::build_request_body).

  ---
  2. Client request format + concrete example

  This is the standard Anthropic Messages API. Endpoint, headers, and body shape are enforced by api/routes.py +
  api/models/anthropic.py::MessagesRequest.

  - URL: POST http://<host>:8082/v1/messages (default port from Settings.host=0.0.0.0, port=8082)
  - Auth header (one of, see api/dependencies.py::require_api_key):
    - x-api-key: freecc, or
    - Authorization: Bearer freecc, or
    - anthropic-auth-token: freecc
  - Required body fields: model, messages. max_tokens, system, tools, stream, temperature, top_p, top_k, thinking, tool_choice,
  metadata are all optional (extras are accepted, see model_config = ConfigDict(extra="allow")).

  curl example

  curl -N -X POST http://localhost:8082/v1/messages \
    -H "Content-Type: application/json" \
    -H "x-api-key: freecc" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-sonnet-4-20250514",
      "max_tokens": 1024,
      "stream": true,
      "system": "You are a terse assistant.",
      "messages": [
        {"role": "user", "content": "Say hi in 3 words."}
      ]
    }'

  That request will get rewritten to NIM with model="z-ai/glm-5.1" (sonnet → MODEL_SONNET).

  Tool-use example (matches the Claude Code shape)

  {
    "model": "claude-opus-4-20250514",
    "max_tokens": 4096,
    "stream": true,
    "system": [{"type": "text", "text": "You are a coding agent."}],
    "messages": [
      {"role": "user", "content": [{"type": "text", "text": "List files."}]},
      {"role": "assistant", "content": [
        {"type": "tool_use", "id": "tu_1", "name": "bash", "input": {"command": "ls"}}
      ]},
      {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "tu_1", "content": "README.md\nsrc/"}
      ]}
    ],
    "tools": [
      {
        "name": "bash",
        "description": "Run a shell command.",
        "input_schema": {
          "type": "object",
          "properties": {"command": {"type": "string"}},
          "required": ["command"]
        }
      }
    ]
  }

  Response is always an SSE stream (the route hardcodes streaming — see services.py::create_message).

  ---
  3. About WARNING: Invalid HTTP request received.

  This warning isn't from this codebase. A grep confirms it doesn't exist anywhere in free-claude-code. It comes from uvicorn's h11   HTTP parser (uvicorn/protocols/http/h11_impl.py) when h11 raises RemoteProtocolError while parsing the request line/headers —
  i.e. before FastAPI ever sees the request. So a FastAPI exception handler or middleware cannot capture it.

  Common triggers:
  - A client speaking TLS to the plain-HTTP port (e.g. https://localhost:8082 instead of http://)
  - Hitting /health from a browser that sent HTTP/2 preface bytes (b'PRI * ...')
  - A buggy/proxy client sending malformed request lines or oversize headers (h11 has a 16 KiB default for incomplete events)
  - Excel/Office UDFs and similar embedded HTTP clients

  Two practical things you can do:

  (a) Log every valid request body in the console

  Add a tiny ASGI middleware in api/app.py (after app = FastAPI(...)). This will show you exactly what the client sent for the
  requests that do reach FastAPI:

  @app.middleware("http")
  async def log_request(request: Request, call_next):
      body = await request.body()
      logger.info(
          "REQ {} {} headers={} body={}",
          request.method,
          request.url.path,
          dict(request.headers),
          body.decode("utf-8", errors="replace")[:4000],
      )
      return await call_next(request)

  If you want it visible in the console (not just server.log), also re-add a stderr sink in
  config/logging_config.py::configure_logging:

  import sys
  logger.add(sys.stderr, level="INFO")

  (b) Surface the underlying h11 reason instead of the bare warning

  Two options:

  1. Switch uvicorn to httptools (more permissive parser, often makes the warning go away). In cli/entrypoints.py::serve:
  uvicorn.run("api.app:create_app", factory=True, host=settings.host,
              port=settings.port, http="httptools",  # <-- add this
              log_level="debug", timeout_graceful_shutdown=5)
  2. Monkey-patch uvicorn's H11Protocol at startup to log the offending bytes:
  import uvicorn.protocols.http.h11_impl as h11_impl
  _orig = h11_impl.H11Protocol.handle_events
  async def _patched(self):
      try:
          await _orig(self)
      except Exception as exc:
          logger.warning("h11 parse failed peer={} buf={!r} exc={}",
                         self.client, getattr(self.conn, "_receive_buffer", b"")[:200], exc)
          raise
  h11_impl.H11Protocol.handle_events = _patched

  Both let you see the actual bytes/peer instead of the bare "Invalid HTTP request received."