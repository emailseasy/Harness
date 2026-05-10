To run it from your existing env:

  conda activate D:\anaconda3\envs\excel-parser
  python -m pip install --upgrade boto3
  set AWS_BEARER_TOKEN_BEDROCK=<your short-term Bedrock key>
  set AWS_REGION=ca-central-1
  python agents/s01_agent_loop_bedrock.py