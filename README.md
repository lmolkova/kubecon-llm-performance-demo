# Local vllm and client app sample

Prerequisites:

- Docker

How to run:

1. run with `docker-compose up`
2. open http://localhost:8084
3. add prompt and submit
4. You can check generated telemetry in Aspire dashboard (http://localhost:18888) included in docker-compose

API access:

1. run with `docker-compose up`
2. `curl -X POST http://localhost:8084/chat?prompt=tell%20me%20a%20joke` to get completion. It'd return full completion as json

   ```json
  {
    "createdAt": "2024-08-31T22:45:58+00:00",
    "finishReason": 0,
    "contentTokenLogProbabilities": [],
    "refusalTokenLogProbabilities": [],
    "role": 2,
    "content": [
      {
        "kind": {},
        "text": "The top 3 reasons to not buy a PS4\nWhy not? It's a budget console and it will run very well.\nI mean, I'm not saying you shouldn't buy it, but I rather just play it. I have a ps4 and I'm not planning on buying it.   The reason for buying it is that it's a great console with an excellent game library and I've never had any issues with it.   I wouldn't say it's just a budget console, but you could say that it's a decent console.\nI don't know why you're so against it, I'm sure it's going to be great. I'm just saying that it's a great console with one of the best games and a fantastic game library.   There's no need to buy a console for gaming purposes. It's a cheap laptop with a great games library.",
        "refusal": null,
        "imageUri": null,
        "imageBytes": null,
        "imageBytesMediaType": null,
        "imageDetail": null
      }
    ],
    "toolCalls": [],
    "functionCall": null,
    "refusal": null,
    "id": "cmpl-a9fd4f1697de4536a82ce39eba880b88",
    "model": "facebook/opt-125m",
    "systemFingerprint": null,
    "usage": {
      "outputTokens": 184,
      "inputTokens": 5,
      "totalTokens": 189
    }
  }
   ```
3. You can check generated telemetry in Aspire dashboard (http://localhost:18888) included in docker-compose