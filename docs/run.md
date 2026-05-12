
env updated with three vars:
  - AWS_BEARER_TOKEN_BEDROCK — placeholder; replace with your short-term key                                                                                   - AWS_REGION=ca-central-1                                                                                                                                
  - BEDROCK_MODEL_ID=global.amazon.nova-2-lite-v1:0                                                                                                        

python .\Agents\Agent_loop.py
AgentLoop >> how many files in current folder?
Traceback (most recent call last):
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connectionpool.py", line 466, in _make_request
    self._validate_conn(conn)
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connectionpool.py", line 1095, in _validate_conn
    conn.connect()
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connection.py", line 652, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connection.py", line 805, in _ssl_wrap_socket_and_match_hostname 
    ssl_sock = ssl_wrap_socket(
               ^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\util\ssl_.py", line 465, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\util\ssl_.py", line 509, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\ssl.py", line 517, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\ssl.py", line 1104, in _create
    self.do_handshake()
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\ssl.py", line 1382, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006) 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\httpsession.py", line 465, in send
    urllib_response = conn.urlopen(
                      ^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connectionpool.py", line 843, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\util\retry.py", line 449, in increment
    raise reraise(type(error), error, _stacktrace)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\util\util.py", line 39, in reraise
    raise value
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connectionpool.py", line 789, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connectionpool.py", line 490, in _make_request
    raise new_e
urllib3.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)  

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\git\PDP-DataEngineer-Dev\Agent_Harness\Agents\Agent_loop.py", line 104, in <module>
    agent_loop(history)
  File "C:\git\PDP-DataEngineer-Dev\Agent_Harness\Agents\Agent_loop.py", line 67, in agent_loop
    response = client.converse(
               ^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\client.py", line 602, in _api_call
    return self._make_api_call(operation_name, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\context.py", line 123, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\client.py", line 1060, in _make_api_call
    http, parsed_response = self._make_request(
                            ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\client.py", line 1084, in _make_request
    return self._endpoint.make_request(operation_model, request_dict)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\endpoint.py", line 119, in make_request
    return self._send_request(request_dict, operation_model)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\endpoint.py", line 200, in _send_request
    while self._needs_retry(
          ^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\endpoint.py", line 360, in _needs_retry
    responses = self._event_emitter.emit(
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\hooks.py", line 412, in emit
    return self._emitter.emit(aliased_event_name, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\hooks.py", line 256, in emit
    return self._emit(event_name, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\hooks.py", line 239, in _emit
    response = handler(**kwargs)
               ^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\retryhandler.py", line 207, in __call__
    if self._checker(**checker_kwargs):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\retryhandler.py", line 284, in __call__
    should_retry = self._should_retry(
                   ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\retryhandler.py", line 320, in _should_retry
    return self._checker(attempt_number, response, caught_exception)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\retryhandler.py", line 363, in __call__
    checker_response = checker(
                       ^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\retryhandler.py", line 247, in __call__
    return self._check_caught_exception(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\retryhandler.py", line 416, in _check_caught_exception
    raise caught_exception
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\endpoint.py", line 279, in _do_get_response
    http_response = self._send(request)
                    ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\endpoint.py", line 383, in _send
    return self.http_session.send(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\httpsession.py", line 492, in send
    raise SSLError(endpoint_url=request.url, error=e)
botocore.exceptions.SSLError: SSL validation failed for https://bedrock-runtime.ca-central-1.amazonaws.com/model/global.amazon.nova-2-lite-v1%3A0/converse [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)
