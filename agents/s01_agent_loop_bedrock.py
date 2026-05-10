#!/usr/bin/env python3
"""
s01_agent_loop_bedrock.py - The Agent Loop, AWS Bedrock variant

Same loop as s01_agent_loop.py, driven by AWS Bedrock's Converse API
with Amazon Nova 2 Lite. Only dependency is boto3.

Auth: standard boto3 credential chain. Either set AWS_BEARER_TOKEN_BEDROCK
(short-term Bedrock API key) or AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY.
Region defaults to ca-central-1; override with AWS_REGION.
Model defaults to global.amazon.nova-2-lite-v1:0; override with BEDROCK_MODEL_ID.
"""

import os
import subprocess

try:
    import readline
    readline.parse_and_bind('set bind-tty-special-chars off')
    readline.parse_and_bind('set input-meta on')
    readline.parse_and_bind('set output-meta on')
    readline.parse_and_bind('set convert-meta off')
    readline.parse_and_bind('set enable-meta-keybindings on')
except ImportError:
    pass

import boto3

MODEL = os.getenv("BEDROCK_MODEL_ID", "global.amazon.nova-2-lite-v1:0")
REGION = os.getenv("AWS_REGION", "ca-central-1")
client = boto3.client("bedrock-runtime", region_name=REGION)

SYSTEM = (f"You are a coding agent at {os.getcwd()}. Use bash to solve tasks. "
          "Before act explain why you will do, then act, after act explain "
          "what you will do next if there are any.")

TOOL_CONFIG = {"tools": [{"toolSpec": {
    "name": "bash",
    "description": "Run a shell command.",
    "inputSchema": {"json": {
        "type": "object",
        "properties": {"command": {"type": "string"}},
        "required": ["command"],
    }},
}}]}

REASONING = {"reasoningConfig": {"type": "enabled", "maxReasoningEffort": "low"}}


def run_bash(command: str) -> str:
    dangerous = ["rm -rf /", "sudo", "shutdown", "reboot", "> /dev/"]
    if any(d in command for d in dangerous):
        return "Error: Dangerous command blocked"
    try:
        r = subprocess.run(command, shell=True, cwd=os.getcwd(),
                           capture_output=True, text=True, timeout=120)
        out = (r.stdout + r.stderr).strip()
        return out[:50000] if out else "(no output)"
    except subprocess.TimeoutExpired:
        return "Error: Timeout (120s)"
    except (FileNotFoundError, OSError) as e:
        return f"Error: {e}"


def agent_loop(messages: list):
    while True:
        response = client.converse(
            modelId=MODEL,
            system=[{"text": SYSTEM}],
            messages=messages,
            toolConfig=TOOL_CONFIG,
            inferenceConfig={"maxTokens": 8000},
            additionalModelRequestFields=REASONING,
        )
        msg = response["output"]["message"]
        messages.append(msg)
        if response["stopReason"] != "tool_use":
            return
        results = []
        for block in msg["content"]:
            if "toolUse" in block:
                tu = block["toolUse"]
                cmd = tu["input"]["command"]
                print(f"\033[33m$ {cmd}\033[0m")
                out = run_bash(cmd)
                print(out[:200])
                results.append({"toolResult": {
                    "toolUseId": tu["toolUseId"],
                    "content": [{"text": out}],
                }})
        messages.append({"role": "user", "content": results})


if __name__ == "__main__":
    history = []
    while True:
        try:
            query = input("\033[36ms01 >> \033[0m")
        except (EOFError, KeyboardInterrupt):
            break
        if query.strip().lower() in ("q", "exit", ""):
            break
        history.append({"role": "user", "content": [{"text": query}]})
        agent_loop(history)
        last = history[-1]
        if last.get("role") == "assistant":
            for block in last.get("content", []):
                if "text" in block:
                    print(block["text"])
        print()
