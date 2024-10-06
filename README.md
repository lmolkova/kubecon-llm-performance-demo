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

## Chat apps

There are two chat apps with very similar functionality, one in Python another in .NET.
Python one runs on port 8085, .NET on port 8084.

Python one has some issues with telemetry:
- no HTTP or GenAI client metrics (yet)
- some (probably fixable) problems with HTTP server metrics - the histogram boundaries are wrong.

## Run vLLM on CPU

To run, vLLM on CPU instead of GPU, you need to build the vLLM CPU docker image using the
following commands.

```
git clone https://github.com/vllm-project/vllm.git
cd vllm
docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g .
```

Once you have the vLLM image, you can run the following to bring up the vLLM
container along with the client applications.

```
docker-compose -f docker-compose-vllm-cpu.yaml up
```

## Checking telemetry

1. **Aspire** Traces, metrics, and logs are exported to local Aspire dashboard available at http://localhost:18888. Best for logs and traces
2. **Prometheus** Metrics are additionally exported to Prometheus on http://localhost:9090. Nothing good to see there
3. **Grafana** shows nice UX for Prometheus metrics at http://localhost:3003. You'll need to import [GenAI client dashboard](./grafana/gen-ai-client-dashboard.json) to see
   ![image](./docs/images/grafana.png)
