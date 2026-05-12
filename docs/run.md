amazon.nova-2-lite-v1:0   →   INFERENCE_PROFILE (没有 ON_DEMAND)                                                                                              
  意思是：在 ca-central-1 当地 Nova 2 Lite 没有直接部署，只能通过 inference profile 调用。所以 amazon.nova-2-lite-v1:0 这个直接 model ID 不可用 — 必须用       profile 前缀（如 global. / us.）。但 global.* 又被 SCP 拒了。                                                                                            

  但 Playground 能用，说明账号里至少有一个 inference profile 是被允许的。 列出来看：

  aws bedrock list-inference-profiles --region ca-central-1 \
    --query "inferenceProfileSummaries[?contains(inferenceProfileId, 'nova-2-lite')].[inferenceProfileId,inferenceProfileName,status]" \
    --output table

  或者干脆把所有都列出来：

  aws bedrock list-inference-profiles --region ca-central-1 --output text | grep -i nova-2-lite

  输出会告诉你账号下能用的 profile 前缀（可能有 us., apac., eu., global., 或者公司自建的 application inference profile）。

  ---
  最有可能可用的几个，按顺序试：

  # 选项 A: US 跨 region（不是 global）
  export BEDROCK_MODEL_ID=us.amazon.nova-2-lite-v1:0
  python Agent_loop.py

  # 选项 B: APAC
  export BEDROCK_MODEL_ID=apac.amazon.nova-2-lite-v1:0

  # 选项 C: EU
  export BEDROCK_MODEL_ID=eu.amazon.nova-2-lite-v1:0

  

  如果其中一个跑通 → 公司 SCP 是按 profile 前缀做的白名单，global. 被拒但其他允许。

  ---
  如果想精准定位 Playground 用的是哪个，浏览器里打开 Playground，F12 → Network 标签 → 发一句话 → 看请求 URL 里有什么。但通常不必，先把上面
  list-inference-profiles 跑一下，结果发我看一下，就基本能定位。


  -----
  ~ $ aws bedrock list-inference-profiles --region ca-central-1 --output text | grep -i nova-2-lite
INFERENCEPROFILESUMMARIES       2025-11-04T23:14:33.804883+00:00        Routes requests to Amazon Nova 2 Lite globally across all supported AWS Regions.        arn:aws:bedrock:ca-central-1:622833591164:inference-profile/global.amazon.nova-2-lite-v1:0        global.amazon.nova-2-lite-v1:0  GLOBAL Amazon Nova 2 Lite       ACTIVE  SYSTEM_DEFINED  2025-11-22T21:08:18.810118+00:00
MODELS  arn:aws:bedrock:::foundation-model/amazon.nova-2-lite-v1:0
MODELS  arn:aws:bedrock:ca-central-1::foundation-model/amazon.nova-2-lite-v1:0
INFERENCEPROFILESUMMARIES       2025-11-07T03:42:29.890902+00:00        Routes requests to Amazon Nova 2 Lite in ca-central-1, us-east-1, us-east-2 and us-west-2.      arn:aws:bedrock:ca-central-1:622833591164:inference-profile/us.amazon.nova-2-lite-v1:0    us.amazon.nova-2-lite-v1:0      US Amazon Nova 2 Lite   ACTIVE  SYSTEM_DEFINED  2025-11-22T21:08:24.665280+00:00
MODELS  arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-2-lite-v1:0
MODELS  arn:aws:bedrock:us-east-2::foundation-model/amazon.nova-2-lite-v1:0
MODELS  arn:aws:bedrock:ca-central-1::foundation-model/amazon.nova-2-lite-v1:0
MODELS  arn:aws:bedrock:us-west-2::foundation-model/amazon.nova-2-lite-v1:0
export BEDROCK_MODEL_ID=us.amazon.nova-2-lite-v1:0
  python Agent_loop.py

  按之前的分析，这条 profile 路由到 ca-central-1 / us-east-1 / us-east-2 / us-west-2 四个 region，全部带具体 region ARN，应该绕过 SCP 拦截。

  跑通了发一下结果！如果还是被拒，再看错误里的 SCP 是不是又拒了别的 ARN 模式。
