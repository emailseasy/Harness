~ $ export BEDROCK_MODEL_ID=global.amazon.nova-2-lite-v1:0
~ $ export AWS_REGION=ca-central-1
~ $ ls -al
total 44
drwxrwxrwx. 4 cloudshell-user cloudshell-user 4096 May 12 16:12 .
drwxr-xr-x. 3 root            root            4096 May 12 17:18 ..
-rw-r--r--. 1 cloudshell-user cloudshell-user 3838 May 12 16:12 Agent_loop.py
-rw-r--r--. 1 cloudshell-user cloudshell-user   18 May 12 03:59 .bash_logout
-rw-r--r--. 1 cloudshell-user cloudshell-user  141 May 12 03:59 .bash_profile
-rw-r--r--. 1 cloudshell-user cloudshell-user  558 May 12 03:59 .bashrc
drwxr-xr-x. 3 cloudshell-user cloudshell-user 4096 May 12 03:59 .config
drwxr-xr-x. 3 cloudshell-user cloudshell-user 4096 May 12 03:59 .local
-rw-r--r--. 1 cloudshell-user cloudshell-user    0 May 12 16:05 .python_history
-rw-------. 1 cloudshell-user cloudshell-user 1822 May 12 16:12 .viminfo
-rw-r--r--. 1 cloudshell-user cloudshell-user  299 May 12 03:59 .zprofile
-rw-r--r--. 1 cloudshell-user cloudshell-user  801 May 12 03:59 .zshrc
~ $ python Agent_loop.py 
readline: enable-meta-keybindings: unknown variable name
AgentLoop >> how many files in current folder?
Traceback (most recent call last):
  File "/home/cloudshell-user/Agent_loop.py", line 104, in <module>
    agent_loop(history)
    ~~~~~~~~~~^^^^^^^^^
  File "/home/cloudshell-user/Agent_loop.py", line 67, in agent_loop
    response = client.converse(
        modelId=MODEL,
    ...<4 lines>...
        additionalModelRequestFields=REASONING,
    )
  File "/usr/local/python3.13/lib64/python3.13/site-packages/botocore/client.py", line 602, in _api_call
    return self._make_api_call(operation_name, kwargs)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.13/lib64/python3.13/site-packages/botocore/context.py", line 123, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/python3.13/lib64/python3.13/site-packages/botocore/client.py", line 1078, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.errorfactory.AccessDeniedException: An error occurred (AccessDeniedException) when calling the Converse operation: User: arn:aws:sts::622833591164:assumed-role/AWSReservedSSO_AdministratorAccess_d6addde423d7eb79/Xiaofei.Jia@cra-arc.gc.ca is not authorized to perform: bedrock:InvokeModel on resource: arn:aws:bedrock:::foundation-model/amazon.nova-2-lite-v1:0 with an explicit deny in a service control policy: arn:aws:organizations::179969298259:policy/o-mo5jvcl5j0/service_control_policy/p-kux2m48e
