#!/usr/bin/env python3
"""Clinical vignette template generator for Tuinalogy CUs."""
from __future__ import annotations

import argparse
from pathlib import Path

PREGNANCY_POINTS = "合谷 LI4、三阴交 SP6、肩井 GB21、至阴 BL67、昆仑 BL60"
SECTIONS = ["患者呈现", "四诊评估", "治疗方案", "预期结果", "禁忌检查"]

PERSONAS = [
    (45, "男", "办公室职员", "反复发作两周，影响工作效率"),
    (32, "女", "运动员", "训练后症状加重，持续一周"),
    (60, "男", "退休教师", "隐痛反复三个月，近日加重"),
    (28, "女", "家庭主妇", "活动受限一月余，日常不便"),
    (55, "男", "建筑工人", "劳累后明显加重，休息难缓解"),
]

CU_META: dict[str, tuple[str, list[str], list[str], list[str]]] = {
    "C01": ("推拿疗法服务咨询", ["颈椎病", "腰椎间盘突出", "肩周炎"],
            ["问诊采集", "望诊观察", "切诊触诊"], ["风池 GB20", "肩井 GB21", "天柱 BL10"]),
    "C02": ("全身推拿服务", ["全身疲劳", "失眠多梦", "气血不畅"],
            ["推法", "揉法", "滚法"], ["百会 GV20", "足三里 ST36", "神门 HT7"]),
    "C03": ("运动推拿服务", ["运动拉伤", "关节扭伤", "肌腱炎"],
            ["弹拨法", "点按法", "摇法"], ["阳陵泉 GB34", "委中 BL40", "悬钟 GB39"]),
    "C04": ("肌肉骨骼推拿服务", ["颈椎退行性变", "腰肌劳损", "膝关节炎"],
            ["正骨手法", "理筋手法", "松解法"], ["大椎 GV14", "肾俞 BL23", "膝眼 EX-LE4"]),
    "C05": ("推拿疗法中心行政管理", ["客户投诉处理", "预约系统管理", "质量改进"],
            ["沟通协调", "记录管理", "流程监控"], []),
    "E01": ("小儿推拿服务", ["小儿发热", "小儿腹泻", "小儿厌食"],
            ["推天河水", "清大肠", "揉板门"], ["天河水", "板门", "六腑"]),
    "E02": ("妇女推拿服务", ["痛经", "产后腰痛", "更年期综合征"],
            ["揉法温通", "推法疏调", "点按补益"], ["关元 CV4", "气海 CV6", "血海 SP10"]),
}


def generate_vignettes(cu_code: str, noss_extract_path: str | Path | None = None) -> str:
    """Generate 3-5 clinical vignettes for the given CU code. Returns markdown."""
    cu = cu_code.upper()
    if cu not in CU_META:
        raise ValueError(f"Unknown CU: {cu}. Valid: {', '.join(sorted(CU_META))}")
    name, conditions, techniques, points = CU_META[cu]
    lines: list[str] = [
        f"# {cu} 临床案例教学情景",
        f"\n**能力单位：** {cu} {name}",
        f"**WIM 编码：** MP-031-3:2016-{cu}/KP(临床案例)",
        "---\n",
    ]
    count = min(len(PERSONAS), max(3, len(conditions) + 1))
    for i in range(count):
        age, gender, occ, complaint = PERSONAS[i]
        cond = conditions[i % len(conditions)]
        tech = techniques[:3] if techniques else ["基础推拿手法"]
        pt = points[:3] if points else ["相关穴位"]
        lines.append(f"## 案例 {i + 1}：{gender}性，{age}岁，{occ}\n")
        lines.append(f"### 患者呈现\n")
        lines.append(
            f"{age}岁{gender}性{occ}，因{cond}前来就诊。主诉{complaint}，"
            f"伴有局部不适感。既往无重大疾病史，无药物过敏，生命体征稳定。\n"
        )
        lines.append("### 四诊评估\n")
        lines.append(f"- **望诊：** 患处局部肌肉紧张，姿态偏移，面色偏暗，舌淡苔白")
        lines.append(f"- **闻诊：** 语声正常，呼吸平稳，偶有叹息，无异常气味")
        lines.append(f"- **问诊：** {cond}症状持续加重，劳累诱发，休息后稍缓解；纳眠一般")
        lines.append(f"- **切诊：** 患处触诊有明显压痛及条索状结节，脉弦细\n")
        lines.append("### 治疗方案\n")
        for j, t in enumerate(tech, 1):
            target = pt[j - 1] if j - 1 < len(pt) else "相关部位"
            lines.append(f"{j}. {t}施于{target}附近（10-15分钟）")
        lines.append(f"{len(tech) + 1}. 善后处理：轻柔拍法放松，嘱咐注意事项\n")
        lines.append("### 预期结果\n")
        lines.append(
            f"经3-5次治疗后，{cond}症状缓解70%以上，活动功能恢复正常。"
            f"建议配合日常保健锻炼，避免诱因，定期复诊评估。\n"
        )
        lines.append("### 禁忌检查\n")
        lines.append(f"- ☐ 确认非妊娠状态（禁忌穴位：{PREGNANCY_POINTS}）")
        lines.append("- ☐ 排除骨折、脱位等急性损伤")
        lines.append("- ☐ 排除急性感染、发热或传染性皮肤病")
        lines.append("- ☐ 检查皮肤完整性（无开放性伤口、严重皮疹）\n---\n")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="生成推拿临床案例教学情景")
    parser.add_argument("--cu", required=True, help="CU code: C01-C05, E01, E02, or 'all'")
    parser.add_argument("--output", default="tuinalogy-services/", help="Output base dir")
    args = parser.parse_args()
    cus = list(CU_META.keys()) if args.cu.lower() == "all" else [args.cu.upper()]
    for cu in cus:
        content = generate_vignettes(cu, Path(args.output) / cu / "00-cocu.md")
        existing_kps = list((Path(args.output) / cu).glob("KP-*.md"))
        seq = len(existing_kps) + 1
        outfile = Path(args.output) / cu / f"KP-{seq:02d}-clinical-vignettes.md"
        outfile.parent.mkdir(parents=True, exist_ok=True)
        outfile.write_text(content, encoding="utf-8")
        print(f"✓ {outfile} ({len(content)} chars, {content.count('## 案例')} vignettes)")


if __name__ == "__main__":
    main()
