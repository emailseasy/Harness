
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

 set NO_PROXY=amazonaws.com,.amazonaws.com
  python agents/s01_agent_loop_bedrock.py
  Or persist it in the conda env:
  conda env config vars set NO_PROXY=amazonaws.com,.amazonaws.com
  conda activate D:\anaconda3\envs\excel-parser
