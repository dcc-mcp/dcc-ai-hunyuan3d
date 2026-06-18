from __future__ import annotations

import json
import os
import shutil
import subprocess
from typing import Any

from dcc_mcp_core.skill import skill_error, skill_success


def region_or_default(region: str | None) -> str:
    return region or os.environ.get("TENCENTCLOUD_REGION") or "ap-guangzhou"


def run_tccli(args: list[str], dry_run: bool = False) -> dict[str, Any]:
    command = ["tccli", "ai3d", *args]
    if dry_run:
        return skill_success("tccli command prepared", command=command)
    if shutil.which("tccli") is None:
        return skill_error(
            "tccli is not installed",
            "missing executable: tccli",
            prompt="Install Tencent Cloud CLI and configure credentials before using Hunyuan3D.",
            possible_solutions=[
                "pip install tccli",
                "Run tccli configure",
                "Set TENCENTCLOUD_REGION or pass region explicitly",
            ],
            command=command,
        )

    proc = subprocess.run(command, capture_output=True, text=True, timeout=60)
    stdout = proc.stdout.strip()
    stderr = proc.stderr.strip()
    try:
        parsed = json.loads(stdout) if stdout else {}
    except json.JSONDecodeError:
        parsed = {"raw_stdout": stdout}

    if proc.returncode != 0:
        return skill_error(
            "tccli command failed",
            stderr or stdout or f"exit code {proc.returncode}",
            command=command,
            response=parsed,
        )

    return skill_success("tccli command completed", command=command, response=parsed)

