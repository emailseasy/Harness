aws bedrock list-foundation-models --region ca-central-1 \                                                                                               
    --query 'modelSummaries[?contains(modelId, `nova`)].[modelId,modelName,inferenceTypesSupported]' \
    --output table
