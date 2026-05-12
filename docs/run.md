
env updated with three vars:
  - AWS_BEARER_TOKEN_BEDROCK — placeholder; replace with your short-term key                                                                                   - AWS_REGION=ca-central-1                                                                                                                                
  - BEDROCK_MODEL_ID=global.amazon.nova-2-lite-v1:0                                                                                                        

  Important caveat: the script does not auto-load .env (we kept it dependency-free, no python-dotenv). Easiest way to actually feed these into the process on   your Anaconda env:

  conda activate D:\anaconda3\envs\excel-parser
  conda env config vars set AWS_BEARER_TOKEN_BEDROCK=<your-key> AWS_REGION=ca-central-1 BEDROCK_MODEL_ID=global.amazon.nova-2-lite-v1:0
  conda activate D:\anaconda3\envs\excel-parser

  (The second conda activate is required — env vars set this way only take effect on next activation.) After that, python agents/s01_agent_loop_bedrock.py
  will pick them up directly.

To run it from your existing env:

  conda activate D:\anaconda3\envs\excel-parser
  python -m pip install --upgrade boto3
  set AWS_BEARER_TOKEN_BEDROCK=<your short-term Bedrock key>
  set AWS_REGION=ca-central-1
  python agents/s01_agent_loop_bedrock.py

  aws bedrock-runtime converse \
--model-id arn:aws:bedrock:ca-central-1:xxxxxxx:inference-profile/global.amazon.nova-2-lite-v1:0
 python .\Agents\Agent_loop.py
AgentLoop >> how many files in current directoru
Traceback (most recent call last):
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connectionpool.py", line 775, in urlopen
    self._prepare_proxy(conn)
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connectionpool.py", line 1044, in _prepare_proxy
    conn.connect()
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connection.py", line 632, in connect
    self._tunnel()  # type: ignore[attr-defined]
    ^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\http\client.py", line 943, in _tunnel   
    raise OSError(f"Tunnel connection failed: {code} {message.strip()}")
OSError: Tunnel connection failed: 407 Proxy Authentication Required

The above exception was the direct cause of the following exception:

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
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\util\util.py", line 38, in reraise
    raise value.with_traceback(tb)
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connectionpool.py", line 775, in urlopen
    self._prepare_proxy(conn)
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connectionpool.py", line 1044, in _prepare_proxy
    conn.connect()
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\urllib3\connection.py", line 632, in connect
    self._tunnel()  # type: ignore[attr-defined]
    ^^^^^^^^^^^^^^
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\http\client.py", line 943, in _tunnel   
    raise OSError(f"Tunnel connection failed: {code} {message.strip()}")
urllib3.exceptions.ProxyError: ('Unable to connect to proxy', OSError('Tunnel connection failed: 407 Proxy Authentication Required'))

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
  File "C:\Users\xxj000\Anaconda3\envs\excel-parser\Lib\site-packages\botocore\httpsession.py", line 496, in send
    raise ProxyConnectionError(
botocore.exceptions.ProxyConnectionError: Failed to connect to proxy URL: "http://proxy.omega.dce-eir.net:8080"
