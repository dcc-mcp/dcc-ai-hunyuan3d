from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_error, skill_exception, skill_success

from _tccli import region_or_default, run_tccli


def _action(job_type: str) -> str:
    if job_type == "pro":
        return "SubmitHunyuanTo3DProJob"
    if job_type == "rapid":
        return "SubmitHunyuanTo3DRapidJob"
    raise ValueError("job_type must be pro or rapid")


@skill_entry
def main(
    prompt: str | None = None,
    image_url: str | None = None,
    image_base64: str | None = None,
    job_type: str = "pro",
    model: str = "3.0",
    generate_type: str = "Normal",
    enable_pbr: bool = False,
    face_count: int = 500000,
    result_format: str | None = None,
    region: str | None = None,
    dry_run: bool = False,
    **_: Any,
) -> dict[str, Any]:
    try:
        inputs = [v for v in (prompt, image_url, image_base64) if v]
        if len(inputs) != 1 and generate_type != "Sketch":
            return skill_error(
                "Provide exactly one input",
                "prompt, image_url, and image_base64 are mutually exclusive for normal Hunyuan3D jobs",
            )

        args = [_action(job_type), "--Region", region_or_default(region), "--Model", model]
        if prompt:
            args += ["--Prompt", prompt]
        if image_url:
            args += ["--ImageUrl", image_url]
        if image_base64:
            args += ["--ImageBase64", image_base64]
        if generate_type:
            args += ["--GenerateType", generate_type]
        if enable_pbr:
            args += ["--EnablePBR", "true"]
        if face_count:
            args += ["--FaceCount", str(face_count)]
        if result_format:
            args += ["--ResultFormat", result_format]

        result = run_tccli(args, dry_run=dry_run)
        response = result.get("response") or {}
        job_id = ((response.get("Response") or {}).get("JobId") if isinstance(response, dict) else None)
        if job_id:
            result["job_id"] = job_id
            result["message"] = "Hunyuan3D job submitted"
        return result
    except Exception as exc:
        return skill_exception(exc, message="Failed to submit Hunyuan3D job")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

