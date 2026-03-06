from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any
from urllib import error, request


DEFAULT_BASE_URL = "https://x666.me"


@dataclass(frozen=True)
class RuntimeSettings:
    base_url: str
    api_key: str
    gemini_model: str
    gpt_model: str


def normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


def load_runtime_settings(
    base_url: str | None = None,
    api_key: str | None = None,
    gemini_model: str | None = None,
    gpt_model: str | None = None,
) -> RuntimeSettings:
    resolved_api_key = api_key or os.getenv("X666_API_KEY", "")
    if not resolved_api_key:
        raise SystemExit("Missing API key. Set X666_API_KEY before running the dual-model pipeline.")

    return RuntimeSettings(
        base_url=normalize_base_url(base_url or os.getenv("X666_BASE_URL", DEFAULT_BASE_URL)),
        api_key=resolved_api_key,
        gemini_model=gemini_model or os.getenv("X666_MODEL_GEMINI", "gemini-3.1-pro-high"),
        gpt_model=gpt_model or os.getenv("X666_MODEL_GPT", "gpt-5.4"),
    )


def chat_completion(
    *,
    base_url: str,
    api_key: str,
    model: str,
    messages: list[dict[str, str]],
    temperature: float | None = 0.7,
) -> str:
    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
    }
    if temperature is not None:
        payload["temperature"] = temperature

    request_url = f"{normalize_base_url(base_url)}/v1/chat/completions"
    body = json.dumps(payload).encode("utf-8")
    http_request = request.Request(
        request_url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with request.urlopen(http_request, timeout=180) as response:
            response_data = json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Model request failed with HTTP {exc.code}: {detail}") from exc
    except error.URLError as exc:
        raise SystemExit(f"Model request failed: {exc}") from exc

    choices = response_data.get("choices") or []
    if not choices:
        raise SystemExit(f"Model response did not include choices: {response_data}")

    message = choices[0].get("message") or {}
    content = message.get("content")
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(item.get("text", ""))
        if parts:
            return "\n".join(parts).strip()

    raise SystemExit(f"Model response did not include usable text content: {response_data}")


def extract_html_document(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        segments = stripped.split("```")
        if len(segments) >= 3:
            stripped = segments[1]
            if stripped.startswith("html"):
                stripped = stripped[4:]
            stripped = stripped.strip()

    lowered = stripped.lower()
    html_start = lowered.find("<!doctype html")
    if html_start == -1:
        html_start = lowered.find("<html")
    if html_start != -1:
        stripped = stripped[html_start:]

    lowered = stripped.lower()
    if "</html>" in lowered:
        closing_index = lowered.rfind("</html>")
        stripped = stripped[: closing_index + len("</html>")]

    return stripped.strip()
