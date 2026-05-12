
aws bedrock list-foundation-models --region ca-central-1 --output text | grep -i nova
MODELSUMMARIES  arn:aws:bedrock:ca-central-1::foundation-model/amazon.nova-lite-v1:0    amazon.nova-lite-v1:0   Nova Lite       Amazon  True
MODELSUMMARIES  arn:aws:bedrock:ca-central-1::foundation-model/amazon.nova-2-lite-v1:0  amazon.nova-2-lite-v1:0 Nova 2 Lite     Amazon  True

✅ Nova 2 Lite 在这个账号 + ca-central-1 是可见的。 接下来确认能不能调用。

  1. 看 inference 类型（确认必须用 profile）：                                                                                                                 aws bedrock list-foundation-models --region ca-central-1 \
    --query "modelSummaries[?contains(modelId, 'nova-2-lite')].[modelId,inferenceTypesSupported]" \                                                              --output table                                                                                                                                         

  预期会看到 INFERENCE_PROFILE（和之前账号一样，ca-central-1 当地没有 ON_DEMAND 直接部署）→ 必须走 profile 前缀。

  2. 看哪些 profile 可用：
  aws bedrock list-inference-profiles --region ca-central-1 --output text | grep -i nova-2-lite

  预期能看到 global.amazon.nova-2-lite-v1:0 和 us.amazon.nova-2-lite-v1:0。

  ---
  3. 直接试跑（这个账号没有 SCP 限制，global.* 应该能用）：

  export AWS_PROFILE=<profilename>
  export AWS_REGION=ca-central-1
  export BEDROCK_MODEL_ID=global.amazon.nova-2-lite-v1:0
  python3 Agent_loop.py

  ---
  如果跑出 AccessDeniedException，最常见是 model access 没启用。去 Bedrock console:
  - Region: ca-central-1
  - 左边菜单 → Model access
  - 看 Amazon Nova 2 Lite 状态是不是 Access granted
  - 不是的话点 Request access（Amazon 自家模型几分钟就批）

  ---
  直接跑第 3 步，看会得到什么。AccessDenied / 正常输出 / 其他错误 → 都贴出来就能继续诊断。

Linux bash 版本完整流程：                        

  ---                                                                                                                                                          1️⃣  环境检查
                                                                                                                                                               # Python（Linux 一般是 python3）                                                                                                                         
  python3 --version          # 应该 >= 3.8

  # boto3 版本（需要 >= 1.39.0）
  python3 -c "import boto3; print(boto3.__version__)"

  # 如果没装或太老
  pip3 install --user --upgrade boto3

  # AWS CLI（用于诊断）
  aws --version              # 没有的话: pip3 install --user awscli

  ---
  2️⃣  网络检查

  # 代理变量
  echo "HTTPS_PROXY=$HTTPS_PROXY"
  echo "HTTP_PROXY=$HTTP_PROXY"
  echo "NO_PROXY=$NO_PROXY"

  # 直连 Bedrock 测试
  curl -sI https://bedrock.ca-central-1.amazonaws.com | head -1

  返回 HTTP/2 403/404 ⇒ OK（能联通，缺凭据而已）。如果 timeout/connection refused/SSL error ⇒ 网络问题。

  ---
  3️⃣  设置 AWS 凭据

  选项 A：access key（推荐用于新账号）
  export AWS_ACCESS_KEY_ID="AKIA..."
  export AWS_SECRET_ACCESS_KEY="...."
  export AWS_REGION="ca-central-1"

  选项 B：Bedrock 短期 API key
  export AWS_BEARER_TOKEN_BEDROCK="xxxxxxx="
  export AWS_REGION="ca-central-1"

  ---
  4️⃣  验证身份和权限

  # 身份（应返回新账号的 ARN）
  aws sts get-caller-identity

  # Nova 2 Lite 是否在这个账号 + region 里可见
  aws bedrock list-foundation-models --region ca-central-1 \
    --query "modelSummaries[?contains(modelId, 'nova-2-lite')].[modelId,inferenceTypesSupported]" \
    --output table

  # 看能用哪些 inference profile 前缀
  aws bedrock list-inference-profiles --region ca-central-1 --output text | grep -i nova-2-lite

  ---
  5️⃣  设置脚本要用的变量

  export BEDROCK_MODEL_ID="global.amazon.nova-2-lite-v1:0"
  # 如果 global 被 SCP 拒，换:
  # export BEDROCK_MODEL_ID="us.amazon.nova-2-lite-v1:0"

  ---
  6️⃣  跑

  python3 Agent_loop.py

  ---
  一键检查脚本（拷贝粘贴一次跑完）

  echo "=== Python ==="
  python3 --version
  python3 -c "import boto3; print('boto3', boto3.__version__)"

  echo -e "\n=== Proxy ==="
  echo "HTTPS_PROXY=$HTTPS_PROXY"
  echo "HTTP_PROXY=$HTTP_PROXY"
  echo "NO_PROXY=$NO_PROXY"

  echo -e "\n=== Network to Bedrock ==="
  curl -sI https://bedrock.${AWS_REGION:-ca-central-1}.amazonaws.com | head -1

  echo -e "\n=== AWS Identity ==="
  aws sts get-caller-identity

  echo -e "\n=== Bedrock model access ==="
  aws bedrock list-foundation-models --region "${AWS_REGION:-ca-central-1}" \
    --query "modelSummaries[?contains(modelId, 'nova-2-lite')].[modelId,inferenceTypesSupported]" \
    --output table

  echo -e "\n=== Env vars for script ==="
  echo "AWS_REGION=$AWS_REGION"
  echo "BEDROCK_MODEL_ID=$BEDROCK_MODEL_ID"
  echo "AWS_BEARER_TOKEN_BEDROCK=${AWS_BEARER_TOKEN_BEDROCK:+(set, hidden)}"

  ---
  保存到一个文件方便重复用：
  cat > ~/check.sh << 'EOF'
  #!/usr/bin/env bash
  # 把上面那段一键检查脚本内容粘贴在这里
  EOF
  chmod +x ~/check.sh
  ~/check.sh

  ---
  最常见的两个失败点：
  1. aws sts get-caller-identity 报错 ⇒ 凭据没设
  2. list-foundation-models 空或 AccessDenied ⇒ 这个账号还没在 Bedrock console 启用 Nova 2 Lite 的 model access（ca-central-1 region 下点 Request access）

  通过 1-4 步后基本稳了。任何一步卡住把输出贴过来。
