  aws bedrock list-foundation-models --region ca-central-1 \                                                                                                     --query "modelSummaries[?contains(modelId, 'nova')].[modelId,modelName,inferenceTypesSupported]" \                                                     
    --output table

  ---
  或者更简单粗暴——不用 JMESPath，直接 grep：

  aws bedrock list-foundation-models --region ca-central-1 --output text | grep -i nova
