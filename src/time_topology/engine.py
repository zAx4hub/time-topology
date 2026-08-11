"""time-topology engine — zAx4hub (algo=lcs)."""
from __future__ import annotations

import hashlib
import re
from typing import Any


def _tokens(text: str) -> list[str]:
    return [t for t in re.split(r"[^a-z0-9]+", text.lower()) if t]


def _hash01(text: str, seed: int = 0) -> float:
    h = hashlib.blake2b(f"{seed}:{text}".encode(), digest_size=8).digest()
    return int.from_bytes(h, "big") / 2**64


def similarity(a: str, b: str) -> float:
    A, B = set(_tokens(a)), set(_tokens(b))
    if not A and not B:
        return 1.0
    inter = len(A & B)
    return inter / (len(A) + len(B) - inter)


def rank(text: str, seed: int = 78) -> float:
    toks = _tokens(text)
    if not toks:
        return 0.0
    uniq = len(set(toks)) / len(toks)
    rolling = sum(_hash01(t, seed + i) for i, t in enumerate(toks)) / len(toks)
    length_bias = min(1.0, len(toks) / 12)
    score = 0.4 * uniq + 0.4 * rolling + 0.2 * length_bias
    if "lcs" == "markov":
        score = min(1.0, score * 1.03)
    return round(score, 3)


def run(payload: dict[str, Any] | None = None) -> dict[str, Any]:
    payload = payload or {}
    items = payload.get("items") or [{"text": "time-topology"}]
    threshold = float(payload.get("threshold", 0.35))
    seed = int(payload.get("seed", 78))
    baseline = payload.get("baseline", "")
    findings = []
    for i, it in enumerate(items):
        text = it["text"] if isinstance(it, dict) else str(it)
        weight = float(it.get("weight", 1)) if isinstance(it, dict) else 1.0
        base = rank(text, seed + i) * weight
        sim = similarity(text, baseline) if baseline else 0.0
        score = round(min(1.0, base * 0.85 + sim * 0.15), 3)
        findings.append(
            {
                "id": (it.get("id") if isinstance(it, dict) else None) or f"item-{i+1}",
                "text": text,
                "score": score,
                "tag": "pass" if score >= threshold else "review",
            }
        )
    avg = round(sum(f["score"] for f in findings) / len(findings), 3)
    return {
        "project": "time-topology",
        "author": "zAx4hub",
        "algo": "lcs",
        "summary": f"Processed {len(findings)} items; avg={avg}",
        "score": avg,
        "findings": findings,
        "metrics": {
            "count": len(findings),
            "threshold": threshold,
            "passed": sum(1 for f in findings if f["tag"] == "pass"),
            "id": 78,
        },
    }


def demo() -> dict[str, Any]:
    return run(
        {
            "items": [
                {"text": "Calendar for energy/context switching"},
                {"text": "zAx4hub quality gate regression fixture"},
                {"text": "deterministic lcs scoring path"},
            ],
            "threshold": 0.2,
            "baseline": "zAx4hub open source",
        }
    )


def inspect() -> dict[str, Any]:
    return {
        "name": "time-topology",
        "author": "zAx4hub",
        "oneLiner": "Calendar for energy/context switching",
        "algo": "lcs",
        "version": "0.1.0",
    }
