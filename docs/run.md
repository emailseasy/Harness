~ $ aws bedrock list-foundation-models --region ca-central-1  --query "modelSummaries[?contains(modelId, 'nova')].[modelId,modelName,inferenceTypesSupported]" --output table
-----------------------------
|   ListFoundationModels    |
+---------------------------+
|  amazon.nova-lite-v1:0    |
|  Nova Lite                |
|  INFERENCE_PROFILE        |
|  amazon.nova-2-lite-v1:0  |
|  Nova 2 Lite              |
|  INFERENCE_PROFILE        |
+---------------------------+
