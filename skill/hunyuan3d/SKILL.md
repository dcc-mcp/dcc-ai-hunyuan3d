---
name: hunyuan3d
description: Submit and query Tencent Cloud Hunyuan 3D text/image generation jobs through tccli.
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    display_name: Hunyuan3D
    group: asset.ai.generation
    default_icon: cube
    affinity: any
    marketplace: dcc-ai-hunyuan3d
    tools: tools.yaml
    execution: sync
    permissions:
      - network
    examples:
      - "Submit a Hunyuan 3D Pro text-to-model job"
      - "Submit a Hunyuan 3D image-to-model job"
      - "Query a Hunyuan 3D job by ID"
    contact:
      name: dcc-mcp team
      url: https://github.com/dcc-mcp/dcc-ai-hunyuan3d
    install:
      add_source: "dcc-mcp-cli marketplace add dcc-mcp/dcc-ai-hunyuan3d"
      then_install: "dcc-mcp-cli marketplace install dcc-ai-hunyuan3d"
---

# Hunyuan3D

Use this skill when an agent needs Tencent Cloud Hunyuan 3D generation from a
text prompt or an image URL. It delegates signing, credentials, and endpoint
selection to `tccli`.

Do not use this skill for local open-source Hunyuan3D inference. Use a local
model runtime skill for that.
