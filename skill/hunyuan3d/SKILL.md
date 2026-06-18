---
name: hunyuan3d
description: Submit and query Tencent Cloud Hunyuan 3D text/image generation jobs through tccli.
license: MIT
compatibility: "dcc-mcp-core 0.18+"
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    layer: domain
    tags:
      - ai
      - hunyuan
      - hunyuan3d
      - 3d-generation
      - text-to-3d
      - image-to-3d
    search-hint: "hunyuan 3d, hunyuan3d, tencent cloud ai3d, text to 3d, image to 3d, model generation, tccli"
    tools: tools.yaml
---

# Hunyuan3D

Use this skill when an agent needs Tencent Cloud Hunyuan 3D generation from a
text prompt or an image URL. It delegates signing, credentials, and endpoint
selection to `tccli`.

Do not use this skill for local open-source Hunyuan3D inference. Use a local
model runtime skill for that.
