"""Utility to extract Related Knowledge (RK) items from NOSS CoCU extract files.

Supports two NOSS extract formats:
- BEV / Aesthetic: WA-scoped items numbered N.M (e.g. 1.1, 2.3)
- IT: CU-scoped items numbered KN (e.g. K1, K2)
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

_CU_CODE_LINE = re.compile(r"\*\*CU Code:\*\*\s*.+-C(\d+)")
_WA_HEADING = re.compile(r"^#{2,5}\s+WA\s*(\d+):", re.MULTILINE)
_RK_ITEM = re.compile(r"^\s*-\s+(\d+\.\d+)\s+(.*)")
_IT_CU_HEADING = re.compile(r"^##\s+CU(\d+):", re.MULTILINE)
_IT_K_ITEM = re.compile(r"^\s*-\s+(K\d+):\s+(.*)")


@dataclass
class RKItem:
    cu: str          # e.g. "C01"
    wa: str          # e.g. "1" or "all"
    code: str        # e.g. "1.1" or "K1"
    description: str


def parse_bev_aesthetic(content: str) -> list[RKItem]:
    """Parse BEV/Aesthetic NOSS extract (WA-scoped N.M items)."""
    items: list[RKItem] = []
    cu = "C00"
    wa = "0"
    in_rk = False

    for line in content.splitlines():
        cu_m = _CU_CODE_LINE.search(line)
        if cu_m:
            cu = f"C{int(cu_m.group(1)):02d}"
            wa = "0"
            in_rk = False
            continue

        wa_m = _WA_HEADING.match(line)
        if wa_m:
            wa = wa_m.group(1)
            in_rk = False
            continue

        if "**Related Knowledge:**" in line:
            in_rk = True
            continue

        if in_rk:
            stripped = line.strip()
            if stripped and not stripped.startswith("-"):
                in_rk = False
                continue
            rk_m = _RK_ITEM.match(line)
            if rk_m:
                items.append(
                    RKItem(cu=cu, wa=wa, code=rk_m.group(1), description=rk_m.group(2).strip())
                )

    return items


def parse_it(content: str) -> list[RKItem]:
    """Parse IT NOSS extract (CU-scoped KN items)."""
    items: list[RKItem] = []
    cu = "C00"

    for line in content.splitlines():
        cu_m = _IT_CU_HEADING.match(line)
        if cu_m:
            cu = f"C{int(cu_m.group(1)):02d}"
            continue
        k_m = _IT_K_ITEM.match(line)
        if k_m:
            items.append(RKItem(cu=cu, wa="all", code=k_m.group(1), description=k_m.group(2).strip()))

    return items


def parse_noss_extract(noss_file: Path, subject: str) -> list[RKItem]:
    """Parse a NOSS extract .md file and return all RK items."""
    content = noss_file.read_text(encoding="utf-8")
    if subject == "it":
        return parse_it(content)
    return parse_bev_aesthetic(content)
