aws: [ERROR]: Unknown function: contain()
~ $ aws bedrock list-foundation-models --region ca-central-1 --query 'modelSummaries[?contains(modelId, nova)].[modelId,modelName,inferenceTypesSupported]' --output table

aws: [ERROR]: 'in <string>' requires string as left operand, not NoneType
