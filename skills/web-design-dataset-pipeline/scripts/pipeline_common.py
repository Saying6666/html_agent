from __future__ import annotations

import http.client
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
    normalized = base_url.rstrip("/")
    if normalized.lower().endswith("/v1"):
        normalized = normalized[:-3]
    return normalized


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
    max_output_tokens: int | None = None,
) -> str:
    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if max_output_tokens is not None:
        payload["max_tokens"] = max_output_tokens

    request_url = f"{normalize_base_url(base_url)}/v1/chat/completions"
    try:
        response_data = post_json(request_url=request_url, api_key=api_key, payload=payload)
        return extract_chat_completions_text(response_data)
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        if exc.code == 400 and "Unsupported legacy protocol" in detail and "/v1/responses" in detail:
            response_url = f"{normalize_base_url(base_url)}/v1/responses"
            response_payload = {
                "model": model,
                "input": [
                    {
                        "role": message["role"],
                        "content": [{"type": "input_text", "text": message["content"]}],
                    }
                    for message in messages
                ],
            }
            if temperature is not None:
                response_payload["temperature"] = temperature
            if max_output_tokens is not None:
                response_payload["max_output_tokens"] = max_output_tokens

            try:
                response_data = post_json(request_url=response_url, api_key=api_key, payload=response_payload)
            except error.HTTPError as retry_exc:
                retry_detail = retry_exc.read().decode("utf-8", errors="replace")
                raise SystemExit(f"Model request failed with HTTP {retry_exc.code}: {retry_detail}") from retry_exc
            except error.URLError as retry_exc:
                raise SystemExit(f"Model request failed: {retry_exc}") from retry_exc
            except http.client.RemoteDisconnected as retry_exc:
                raise SystemExit(f"Model request failed: {retry_exc}") from retry_exc

            return extract_responses_text(response_data)

        raise SystemExit(f"Model request failed with HTTP {exc.code}: {detail}") from exc
    except error.URLError as exc:
        raise SystemExit(f"Model request failed: {exc}") from exc
    except http.client.RemoteDisconnected as exc:
        raise SystemExit(f"Model request failed: {exc}") from exc


def post_json(*, request_url: str, api_key: str, payload: dict[str, Any]) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    http_request = request.Request(
        request_url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) CodexCLI/1.0",
        },
        method="POST",
    )

    with request.urlopen(http_request, timeout=180) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_chat_completions_text(response_data: dict[str, Any]) -> str:
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


def extract_responses_text(response_data: dict[str, Any]) -> str:
    output_text = response_data.get("output_text")
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    parts: list[str] = []
    output = response_data.get("output") or []
    if isinstance(output, list):
        for item in output:
            if not isinstance(item, dict):
                continue
            content = item.get("content") or []
            if not isinstance(content, list):
                continue
            for block in content:
                if not isinstance(block, dict):
                    continue
                if block.get("type") in {"output_text", "text"}:
                    text = block.get("text")
                    if isinstance(text, str) and text.strip():
                        parts.append(text)

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
