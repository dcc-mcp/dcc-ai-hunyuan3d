from __future__ import annotations

import importlib.util
import gzip
import os
import sys
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "hunyuan3d"
SCRIPTS = SKILL / "scripts"


def load(name: str):
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def validate_skill() -> None:
    from dcc_mcp_core import validate_skill

    report = validate_skill(str(SKILL))
    assert not report.has_errors, report


def dry_run_submit() -> None:
    mod = load("submit_hunyuan3d_job")
    result = mod.main(prompt="a small wooden chair", dry_run=True)
    assert result["success"], result
    command = result["context"]["command"]
    assert "tccli" == command[0]
    assert "SubmitHunyuanTo3DProJob" in command
    assert "--Prompt" in command


def live_docs_smoke() -> None:
    if os.environ.get("RUN_LIVE_API_SMOKE") != "true":
        print("skip live Tencent Cloud docs smoke")
        return
    url = "https://cloud.tencent.com/document/product/1804/120838"
    req = urllib.request.Request(url, headers={"User-Agent": "dcc-mcp-hunyuan3d-ci/0.1"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
    try:
        text = gzip.decompress(raw).decode("utf-8", "ignore")
    except gzip.BadGzipFile:
        text = raw.decode("utf-8", "ignore")
    for action in (
        "SubmitHunyuanTo3DProJob",
        "QueryHunyuanTo3DProJob",
        "SubmitHunyuanTo3DRapidJob",
        "QueryHunyuanTo3DRapidJob",
    ):
        assert action in text, action


def main() -> None:
    validate_skill()
    dry_run_submit()
    live_docs_smoke()


if __name__ == "__main__":
    main()
