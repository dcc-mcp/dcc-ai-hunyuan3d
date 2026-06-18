from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception

from _tccli import region_or_default, run_tccli


def _action(job_type: str) -> str:
    if job_type == "pro":
        return "QueryHunyuanTo3DProJob"
    if job_type == "rapid":
        return "QueryHunyuanTo3DRapidJob"
    raise ValueError("job_type must be pro or rapid")


@skill_entry
def main(
    job_id: str,
    job_type: str = "pro",
    region: str | None = None,
    dry_run: bool = False,
    **_: Any,
) -> dict[str, Any]:
    try:
        args = [_action(job_type), "--Region", region_or_default(region), "--JobId", job_id]
        return run_tccli(args, dry_run=dry_run)
    except Exception as exc:
        return skill_exception(exc, message="Failed to query Hunyuan3D job")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

