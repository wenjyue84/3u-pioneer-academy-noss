"""
NOSS IT-020 Textbook Illustration Generator
Generates technical diagrams as PNG files for embedding in .docx textbooks.
Usage: uv run --with matplotlib scripts/generate_illustrations.py
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "content" / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Consistent styling
COLORS = {
    "primary": "#1F4E79",
    "secondary": "#2E75B6",
    "accent": "#4A90D9",
    "light": "#D6E4F0",
    "bg": "#F8FAFC",
    "text": "#333333",
    "success": "#27AE60",
    "warning": "#F39C12",
    "danger": "#E74C3C",
    "gray": "#95A5A6",
    "white": "#FFFFFF",
}

DPI = 150


def style_axis(ax, title=""):
    ax.set_facecolor(COLORS["bg"])
    ax.set_aspect("equal")
    ax.axis("off")
    if title:
        ax.set_title(title, fontsize=14, fontweight="bold", color=COLORS["primary"], pad=15)


def draw_box(ax, x, y, w, h, label, color=None, fontsize=8, text_color="white"):
    c = color or COLORS["primary"]
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.05", facecolor=c,
                         edgecolor="#1a3d5c", linewidth=1.2)
    ax.add_patch(box)
    ax.text(x, y, label, ha="center", va="center", fontsize=fontsize,
            fontweight="bold", color=text_color, wrap=True)


def draw_circle_node(ax, x, y, r, label, color=None, fontsize=7):
    c = color or COLORS["secondary"]
    circle = Circle((x, y), r, facecolor=c, edgecolor="#1a3d5c", linewidth=1.2)
    ax.add_patch(circle)
    ax.text(x, y, label, ha="center", va="center", fontsize=fontsize,
            fontweight="bold", color="white")


def draw_arrow(ax, x1, y1, x2, y2, color=None):
    c = color or COLORS["gray"]
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-", color=c, lw=1.5))


def draw_arrow_headed(ax, x1, y1, x2, y2, color=None):
    c = color or COLORS["gray"]
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=c, lw=1.5))


# ── 1. Network Topologies ────────────────────────────────────────

def gen_network_topologies():
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.patch.set_facecolor("white")
    fig.suptitle("Common Network Topologies", fontsize=16, fontweight="bold",
                 color=COLORS["primary"], y=0.97)

    # Star topology
    ax = axes[0, 0]
    style_axis(ax, "Star Topology")
    draw_circle_node(ax, 0.5, 0.5, 0.08, "Switch", COLORS["primary"], 7)
    positions = [(0.5, 0.9), (0.15, 0.7), (0.85, 0.7), (0.15, 0.3), (0.85, 0.3), (0.5, 0.1)]
    for i, (px, py) in enumerate(positions):
        draw_circle_node(ax, px, py, 0.06, f"PC{i+1}", COLORS["accent"], 6)
        draw_arrow(ax, 0.5, 0.5, px, py, COLORS["secondary"])
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)

    # Bus topology
    ax = axes[0, 1]
    style_axis(ax, "Bus Topology")
    ax.plot([0.1, 0.9], [0.5, 0.5], color=COLORS["primary"], linewidth=3)
    ax.plot([0.1, 0.1], [0.48, 0.52], color=COLORS["primary"], linewidth=3)
    ax.plot([0.9, 0.9], [0.48, 0.52], color=COLORS["primary"], linewidth=3)
    for i, x in enumerate([0.2, 0.35, 0.5, 0.65, 0.8]):
        draw_circle_node(ax, x, 0.3, 0.06, f"PC{i+1}", COLORS["accent"], 6)
        draw_arrow(ax, x, 0.5, x, 0.36, COLORS["secondary"])
    ax.text(0.5, 0.62, "Backbone Cable", ha="center", fontsize=8, color=COLORS["text"])
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(0.1, 0.75)

    # Ring topology
    ax = axes[1, 0]
    style_axis(ax, "Ring Topology")
    n = 6
    angles = np.linspace(0, 2*np.pi, n, endpoint=False) - np.pi/2
    cx, cy = 0.5, 0.5
    r = 0.3
    pts = [(cx + r * np.cos(a), cy + r * np.sin(a)) for a in angles]
    for i, (px, py) in enumerate(pts):
        draw_circle_node(ax, px, py, 0.06, f"PC{i+1}", COLORS["accent"], 6)
        nx, ny = pts[(i+1) % n]
        draw_arrow_headed(ax, px, py, nx, ny, COLORS["secondary"])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Mesh topology
    ax = axes[1, 1]
    style_axis(ax, "Mesh Topology")
    positions = [(0.3, 0.8), (0.7, 0.8), (0.15, 0.45), (0.85, 0.45), (0.35, 0.15), (0.65, 0.15)]
    for i, (px, py) in enumerate(positions):
        draw_circle_node(ax, px, py, 0.06, f"PC{i+1}", COLORS["accent"], 6)
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            draw_arrow(ax, positions[i][0], positions[i][1],
                       positions[j][0], positions[j][1], "#B4C6E0")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(OUTPUT_DIR / "network-topologies.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: network-topologies.png")


# ── 2. RAID Levels Comparison ─────────────────────────────────────

def gen_raid_levels():
    fig, axes = plt.subplots(1, 4, figsize=(12, 4))
    fig.patch.set_facecolor("white")
    fig.suptitle("RAID Level Comparison", fontsize=16, fontweight="bold",
                 color=COLORS["primary"], y=1.02)

    raids = [
        ("RAID 0\nStriping", ["A1", "A2", "A3", "A4"], ["B1", "B2", "B3", "B4"],
         "Speed: Fast\nRedundancy: None\nMin Disks: 2"),
        ("RAID 1\nMirroring", ["A1", "A1", "", ""], ["A2", "A2", "", ""],
         "Speed: Read fast\nRedundancy: 1 disk\nMin Disks: 2"),
        ("RAID 5\nStriping+Parity", ["A1", "A2", "P"], ["B1", "P", "B2"],
         "Speed: Good\nRedundancy: 1 disk\nMin Disks: 3"),
        ("RAID 10\nMirror+Stripe", ["A1", "A1", "A2", "A2"], ["", "", "", ""],
         "Speed: Fast\nRedundancy: 1 per pair\nMin Disks: 4"),
    ]

    for idx, (title, row1, row2, desc) in enumerate(raids):
        ax = axes[idx]
        ax.set_facecolor(COLORS["bg"])
        ax.axis("off")
        ax.set_title(title, fontsize=10, fontweight="bold", color=COLORS["primary"], pad=10)

        n = len(row1)
        for i, label in enumerate(row1):
            if label:
                color = COLORS["danger"] if label.startswith("P") else COLORS["secondary"]
                rect = FancyBboxPatch((i * 0.22 + 0.05, 0.55), 0.18, 0.25,
                                     boxstyle="round,pad=0.02", facecolor=color,
                                     edgecolor="white", linewidth=1)
                ax.add_patch(rect)
                ax.text(i * 0.22 + 0.14, 0.675, label, ha="center", va="center",
                        fontsize=8, fontweight="bold", color="white")

        for i, label in enumerate(row2):
            if label:
                color = COLORS["danger"] if label.startswith("P") else COLORS["accent"]
                rect = FancyBboxPatch((i * 0.22 + 0.05, 0.25), 0.18, 0.25,
                                     boxstyle="round,pad=0.02", facecolor=color,
                                     edgecolor="white", linewidth=1)
                ax.add_patch(rect)
                ax.text(i * 0.22 + 0.14, 0.375, label, ha="center", va="center",
                        fontsize=8, fontweight="bold", color="white")

        ax.text(0.45, 0.08, desc, ha="center", va="center", fontsize=7,
                color=COLORS["text"], style="italic")
        ax.set_xlim(0, 0.95)
        ax.set_ylim(0, 0.95)

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "raid-levels.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: raid-levels.png")


# ── 3. Troubleshooting Flowchart ──────────────────────────────────

def gen_troubleshooting_flowchart():
    fig, ax = plt.subplots(figsize=(8, 10))
    fig.patch.set_facecolor("white")
    style_axis(ax, "Computer System Troubleshooting Flowchart")

    steps = [
        (0.5, 0.92, "Receive Fault\nReport", COLORS["primary"], 0.14, 0.05),
        (0.5, 0.80, "Gather Symptoms\n(User Interview)", COLORS["secondary"], 0.14, 0.05),
        (0.5, 0.68, "Power ON?", COLORS["warning"], 0.10, 0.04),
        (0.18, 0.58, "Check PSU,\nCables, Switch", COLORS["accent"], 0.12, 0.05),
        (0.5, 0.56, "Display OK?", COLORS["warning"], 0.10, 0.04),
        (0.18, 0.46, "Reseat GPU,\nRAM, Cable", COLORS["accent"], 0.12, 0.05),
        (0.5, 0.44, "OS Boots?", COLORS["warning"], 0.10, 0.04),
        (0.18, 0.34, "Boot USB/\nRepair OS", COLORS["accent"], 0.12, 0.05),
        (0.5, 0.32, "Run Diagnostics\n(Event Log, SMART)", COLORS["secondary"], 0.14, 0.05),
        (0.5, 0.20, "Fault Found?", COLORS["warning"], 0.10, 0.04),
        (0.18, 0.10, "Escalate to\nLevel 2/3", COLORS["danger"], 0.12, 0.05),
        (0.5, 0.08, "Replace/Repair\n& Test", COLORS["success"], 0.14, 0.05),
    ]

    for x, y, label, color, w, h in steps:
        draw_box(ax, x, y, w, h, label, color, fontsize=7)

    # Vertical flow arrows
    for i in [(0, 1), (1, 2), (4, 6), (8, 9)]:
        draw_arrow_headed(ax, 0.5, steps[i[0]][1] - 0.05, 0.5, steps[i[1]][1] + 0.05)

    # Yes arrows (down)
    draw_arrow_headed(ax, 0.5, 0.64, 0.5, 0.60)
    draw_arrow_headed(ax, 0.5, 0.52, 0.5, 0.48)
    draw_arrow_headed(ax, 0.5, 0.40, 0.5, 0.37)
    draw_arrow_headed(ax, 0.5, 0.16, 0.5, 0.13)

    # No arrows (left)
    draw_arrow_headed(ax, 0.40, 0.68, 0.30, 0.62)
    draw_arrow_headed(ax, 0.40, 0.56, 0.30, 0.50)
    draw_arrow_headed(ax, 0.40, 0.44, 0.30, 0.38)
    draw_arrow_headed(ax, 0.40, 0.20, 0.30, 0.14)

    # Labels
    ax.text(0.55, 0.66, "Yes", fontsize=7, color=COLORS["success"], fontweight="bold")
    ax.text(0.36, 0.67, "No", fontsize=7, color=COLORS["danger"], fontweight="bold")
    ax.text(0.55, 0.54, "Yes", fontsize=7, color=COLORS["success"], fontweight="bold")
    ax.text(0.36, 0.55, "No", fontsize=7, color=COLORS["danger"], fontweight="bold")
    ax.text(0.55, 0.42, "Yes", fontsize=7, color=COLORS["success"], fontweight="bold")
    ax.text(0.36, 0.43, "No", fontsize=7, color=COLORS["danger"], fontweight="bold")
    ax.text(0.55, 0.18, "Yes", fontsize=7, color=COLORS["success"], fontweight="bold")
    ax.text(0.36, 0.19, "No", fontsize=7, color=COLORS["danger"], fontweight="bold")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.savefig(OUTPUT_DIR / "troubleshooting-flowchart.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: troubleshooting-flowchart.png")


# ── 4. Server Rack Layout ────────────────────────────────────────

def gen_server_rack():
    fig, ax = plt.subplots(figsize=(6, 10))
    fig.patch.set_facecolor("white")
    style_axis(ax, "Standard 42U Server Rack Layout")

    # Rack outline
    rack = FancyBboxPatch((0.15, 0.05), 0.7, 0.88, boxstyle="round,pad=0.01",
                          facecolor="#E8ECF0", edgecolor=COLORS["primary"], linewidth=2)
    ax.add_patch(rack)

    # Components from top to bottom
    components = [
        (0.87, 0.04, "Patch Panel (1U)", COLORS["gray"]),
        (0.82, 0.04, "Patch Panel (1U)", COLORS["gray"]),
        (0.77, 0.04, "Network Switch (1U)", COLORS["secondary"]),
        (0.72, 0.04, "Network Switch (1U)", COLORS["secondary"]),
        (0.66, 0.04, "Firewall (1U)", COLORS["danger"]),
        (0.60, 0.08, "Server 1 - AD/DNS (2U)", COLORS["primary"]),
        (0.51, 0.08, "Server 2 - File/App (2U)", COLORS["primary"]),
        (0.42, 0.08, "Server 3 - DB (2U)", COLORS["primary"]),
        (0.33, 0.12, "Storage Array (4U)", COLORS["accent"]),
        (0.20, 0.04, "Cable Management (1U)", "#B4C6E0"),
        (0.14, 0.08, "UPS (2U)", COLORS["warning"]),
    ]

    for y, h, label, color in components:
        rect = FancyBboxPatch((0.2, y), 0.6, h, boxstyle="round,pad=0.005",
                              facecolor=color, edgecolor="white", linewidth=1)
        ax.add_patch(rect)
        ax.text(0.5, y + h/2, label, ha="center", va="center",
                fontsize=8, fontweight="bold", color="white")

    # U markings
    for i, u in enumerate(range(42, 0, -1)):
        y = 0.05 + (i * 0.88 / 42)
        if u % 5 == 0:
            ax.text(0.12, y, f"{u}U", ha="right", va="center", fontsize=6, color=COLORS["gray"])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.savefig(OUTPUT_DIR / "server-rack-layout.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: server-rack-layout.png")


# ── 5. Security Zones Diagram ────────────────────────────────────

def gen_security_zones():
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("white")
    style_axis(ax, "Network Security Zones Architecture")

    # Internet cloud
    ax.text(0.08, 0.5, "INTERNET", ha="center", va="center", fontsize=10,
            fontweight="bold", color=COLORS["danger"],
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FDEAEA", edgecolor=COLORS["danger"]))

    # Firewall
    draw_box(ax, 0.28, 0.5, 0.1, 0.15, "Firewall\n/ UTM", COLORS["danger"], 8)

    # DMZ
    dmz = FancyBboxPatch((0.38, 0.25), 0.2, 0.5, boxstyle="round,pad=0.02",
                         facecolor="#FFF8E1", edgecolor=COLORS["warning"], linewidth=2, linestyle="--")
    ax.add_patch(dmz)
    ax.text(0.48, 0.72, "DMZ", ha="center", fontsize=10, fontweight="bold", color=COLORS["warning"])
    draw_box(ax, 0.48, 0.55, 0.12, 0.08, "Web\nServer", COLORS["warning"], 7)
    draw_box(ax, 0.48, 0.38, 0.12, 0.08, "Email\nGateway", COLORS["warning"], 7)

    # Internal firewall
    draw_box(ax, 0.65, 0.5, 0.08, 0.12, "Internal\nFW", COLORS["accent"], 7)

    # Internal LAN
    lan = FancyBboxPatch((0.72, 0.15), 0.25, 0.7, boxstyle="round,pad=0.02",
                         facecolor="#E8F5E9", edgecolor=COLORS["success"], linewidth=2, linestyle="--")
    ax.add_patch(lan)
    ax.text(0.845, 0.82, "INTERNAL LAN", ha="center", fontsize=9, fontweight="bold", color=COLORS["success"])
    draw_box(ax, 0.845, 0.65, 0.14, 0.08, "AD / DNS\nServer", COLORS["primary"], 7)
    draw_box(ax, 0.845, 0.50, 0.14, 0.08, "File / App\nServer", COLORS["primary"], 7)
    draw_box(ax, 0.845, 0.35, 0.14, 0.08, "Workstations", COLORS["secondary"], 7)
    draw_box(ax, 0.845, 0.22, 0.14, 0.08, "Printers /\nPeripherals", COLORS["gray"], 7)

    # Arrows
    draw_arrow_headed(ax, 0.15, 0.5, 0.23, 0.5, COLORS["danger"])
    draw_arrow_headed(ax, 0.33, 0.5, 0.38, 0.5, COLORS["warning"])
    draw_arrow_headed(ax, 0.58, 0.5, 0.61, 0.5, COLORS["accent"])
    draw_arrow_headed(ax, 0.69, 0.5, 0.72, 0.5, COLORS["success"])

    ax.set_xlim(0, 1)
    ax.set_ylim(0.1, 0.9)
    fig.savefig(OUTPUT_DIR / "security-zones.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: security-zones.png")


# ── 6. Asset Lifecycle ────────────────────────────────────────────

def gen_asset_lifecycle():
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("white")
    style_axis(ax, "IT Asset Lifecycle Management")

    stages = [
        ("Planning &\nBudgeting", COLORS["primary"]),
        ("Procurement\n& Receiving", COLORS["secondary"]),
        ("Deployment\n& Tagging", COLORS["accent"]),
        ("Operation\n& Monitoring", COLORS["success"]),
        ("Maintenance\n& Support", COLORS["warning"]),
        ("Retirement\n& Disposal", COLORS["danger"]),
    ]

    n = len(stages)
    angles = np.linspace(0, 2*np.pi, n, endpoint=False) - np.pi/2
    cx, cy = 0.5, 0.48
    r = 0.3

    for i, (label, color) in enumerate(stages):
        x = cx + r * np.cos(angles[i])
        y = cy + r * np.sin(angles[i])
        draw_box(ax, x, y, 0.15, 0.09, label, color, fontsize=7)

        # Arrow to next
        nx = cx + r * np.cos(angles[(i+1) % n])
        ny = cy + r * np.sin(angles[(i+1) % n])
        mx = cx + (r - 0.05) * np.cos((angles[i] + angles[(i+1) % n]) / 2)
        my = cy + (r - 0.05) * np.sin((angles[i] + angles[(i+1) % n]) / 2)
        draw_arrow_headed(ax, x, y, nx, ny, "#B4C6E0")

    # Center label
    ax.text(cx, cy, "ASSET\nLIFECYCLE", ha="center", va="center", fontsize=11,
            fontweight="bold", color=COLORS["primary"])

    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(0.05, 0.92)
    fig.savefig(OUTPUT_DIR / "asset-lifecycle.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: asset-lifecycle.png")


# ── 7. Cable Wiring T568A/B ──────────────────────────────────────

def gen_cable_wiring():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    fig.patch.set_facecolor("white")
    fig.suptitle("RJ45 Cable Wiring Standards", fontsize=16, fontweight="bold",
                 color=COLORS["primary"], y=0.98)

    wire_colors_a = [
        ("#FFFFFF", "#27AE60", "1: White/Green"),
        ("#27AE60", "#27AE60", "2: Green"),
        ("#FFFFFF", "#F39C12", "3: White/Orange"),
        ("#2E75B6", "#2E75B6", "4: Blue"),
        ("#FFFFFF", "#2E75B6", "5: White/Blue"),
        ("#F39C12", "#F39C12", "6: Orange"),
        ("#FFFFFF", "#8B4513", "7: White/Brown"),
        ("#8B4513", "#8B4513", "8: Brown"),
    ]

    wire_colors_b = [
        ("#FFFFFF", "#F39C12", "1: White/Orange"),
        ("#F39C12", "#F39C12", "2: Orange"),
        ("#FFFFFF", "#27AE60", "3: White/Green"),
        ("#2E75B6", "#2E75B6", "4: Blue"),
        ("#FFFFFF", "#2E75B6", "5: White/Blue"),
        ("#27AE60", "#27AE60", "6: Green"),
        ("#FFFFFF", "#8B4513", "7: White/Brown"),
        ("#8B4513", "#8B4513", "8: Brown"),
    ]

    for idx, (wires, title) in enumerate([(wire_colors_a, "T568A"), (wire_colors_b, "T568B")]):
        ax = axes[idx]
        ax.set_facecolor(COLORS["bg"])
        ax.axis("off")
        ax.set_title(title, fontsize=13, fontweight="bold", color=COLORS["primary"], pad=10)

        # Draw RJ45 connector outline
        conn = FancyBboxPatch((0.25, 0.08), 0.5, 0.78, boxstyle="round,pad=0.02",
                              facecolor="#F0F0F0", edgecolor=COLORS["primary"], linewidth=2)
        ax.add_patch(conn)

        for i, (stripe, solid, label) in enumerate(wires):
            y = 0.80 - i * 0.09
            # Wire color bar
            rect = FancyBboxPatch((0.30, y - 0.025), 0.12, 0.05,
                                  boxstyle="round,pad=0.005", facecolor=solid,
                                  edgecolor="white", linewidth=0.5)
            ax.add_patch(rect)
            if stripe != solid:
                # Stripe indicator
                for s in range(3):
                    sx = 0.31 + s * 0.04
                    srect = plt.Rectangle((sx, y - 0.015), 0.015, 0.03,
                                          facecolor=stripe, alpha=0.7)
                    ax.add_patch(srect)
            # Label
            ax.text(0.48, y, label, va="center", fontsize=8, color=COLORS["text"])

        ax.text(0.5, 0.03, "Pin 1 → Pin 8", ha="center", fontsize=8,
                color=COLORS["gray"], style="italic")
        ax.set_xlim(0.15, 0.85)
        ax.set_ylim(-0.02, 0.95)

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(OUTPUT_DIR / "cable-wiring-t568.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: cable-wiring-t568.png")


# ── 8. Maintenance Schedule ──────────────────────────────────────

def gen_maintenance_schedule():
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("white")

    tasks = [
        "Clean vents & heatsinks",
        "Check fan operation",
        "Update OS & antivirus",
        "Verify backups",
        "Check cables & connectors",
        "Check disk health (SMART)",
        "Review event logs",
        "Full system diagnostic",
    ]
    schedule = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    ]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    data = np.array(schedule)
    cmap = matplotlib.colors.ListedColormap(["#F0F0F0", COLORS["secondary"]])
    ax.imshow(data, cmap=cmap, aspect="auto", interpolation="nearest")

    ax.set_xticks(range(12))
    ax.set_xticklabels(months, fontsize=8, fontweight="bold")
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels(tasks, fontsize=9)
    ax.set_title("Preventive Maintenance Schedule (Annual)", fontsize=14,
                 fontweight="bold", color=COLORS["primary"], pad=15)

    for i in range(len(tasks)):
        for j in range(12):
            if data[i, j]:
                ax.text(j, i, "X", ha="center", va="center", fontsize=8,
                        color="white", fontweight="bold")

    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "maintenance-schedule.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: maintenance-schedule.png")


# ── 9. OSI / TCP-IP Model ────────────────────────────────────────

def gen_osi_model():
    fig, axes = plt.subplots(1, 2, figsize=(10, 7))
    fig.patch.set_facecolor("white")
    fig.suptitle("OSI Model vs TCP/IP Model", fontsize=16, fontweight="bold",
                 color=COLORS["primary"], y=0.98)

    # OSI
    ax = axes[0]
    ax.set_facecolor(COLORS["bg"])
    ax.axis("off")
    ax.set_title("OSI Model (7 Layers)", fontsize=12, fontweight="bold", color=COLORS["primary"])

    osi = [
        ("7. Application", COLORS["danger"]),
        ("6. Presentation", COLORS["warning"]),
        ("5. Session", "#F39C12"),
        ("4. Transport", COLORS["success"]),
        ("3. Network", COLORS["accent"]),
        ("2. Data Link", COLORS["secondary"]),
        ("1. Physical", COLORS["primary"]),
    ]
    for i, (label, color) in enumerate(osi):
        y = 0.85 - i * 0.11
        rect = FancyBboxPatch((0.1, y), 0.8, 0.09, boxstyle="round,pad=0.01",
                              facecolor=color, edgecolor="white", linewidth=1)
        ax.add_patch(rect)
        ax.text(0.5, y + 0.045, label, ha="center", va="center", fontsize=10,
                fontweight="bold", color="white")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # TCP/IP
    ax = axes[1]
    ax.set_facecolor(COLORS["bg"])
    ax.axis("off")
    ax.set_title("TCP/IP Model (4 Layers)", fontsize=12, fontweight="bold", color=COLORS["primary"])

    tcpip = [
        ("Application\n(HTTP, FTP, SMTP, DNS)", COLORS["danger"], 0.28),
        ("Transport\n(TCP, UDP)", COLORS["success"], 0.11),
        ("Internet\n(IP, ICMP, ARP)", COLORS["accent"], 0.11),
        ("Network Access\n(Ethernet, Wi-Fi)", COLORS["primary"], 0.22),
    ]
    y = 0.85
    for label, color, h in tcpip:
        rect = FancyBboxPatch((0.1, y - h), 0.8, h, boxstyle="round,pad=0.01",
                              facecolor=color, edgecolor="white", linewidth=1)
        ax.add_patch(rect)
        ax.text(0.5, y - h/2, label, ha="center", va="center", fontsize=10,
                fontweight="bold", color="white")
        y -= h + 0.02

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(OUTPUT_DIR / "osi-tcpip-model.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: osi-tcpip-model.png")


# ── 10. Project Management Lifecycle ──────────────────────────────

def gen_project_lifecycle():
    fig, ax = plt.subplots(figsize=(12, 4))
    fig.patch.set_facecolor("white")
    style_axis(ax, "IT Project Management Lifecycle (PMBOK)")

    phases = [
        ("Initiating", "Define scope\nIdentify stakeholders\nProject charter", COLORS["primary"]),
        ("Planning", "WBS & Gantt chart\nBudget & resources\nRisk register", COLORS["secondary"]),
        ("Executing", "Team management\nVendor coordination\nDeliverables", COLORS["accent"]),
        ("Monitoring\n& Controlling", "Progress tracking\nChange control\nQuality assurance", COLORS["warning"]),
        ("Closing", "UAT sign-off\nLessons learned\nHandover", COLORS["success"]),
    ]

    for i, (title, desc, color) in enumerate(phases):
        x = 0.1 + i * 0.18
        # Phase box
        rect = FancyBboxPatch((x, 0.35), 0.14, 0.35, boxstyle="round,pad=0.015",
                              facecolor=color, edgecolor="white", linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + 0.07, 0.60, title, ha="center", va="center", fontsize=9,
                fontweight="bold", color="white")
        ax.text(x + 0.07, 0.42, desc, ha="center", va="center", fontsize=6.5,
                color="white", style="italic")

        # Phase number
        ax.text(x + 0.07, 0.78, f"Phase {i+1}", ha="center", fontsize=8,
                fontweight="bold", color=color)

        # Arrow to next
        if i < len(phases) - 1:
            draw_arrow_headed(ax, x + 0.15, 0.525, x + 0.17, 0.525, color)

    ax.set_xlim(0.02, 0.98)
    ax.set_ylim(0.2, 0.9)
    fig.savefig(OUTPUT_DIR / "project-lifecycle.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: project-lifecycle.png")


# ── 11. DR Recovery Strategy ─────────────────────────────────────

def gen_dr_strategy():
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("white")
    style_axis(ax, "Disaster Recovery Site Types — RTO vs Cost")

    sites = [
        ("Cold Site", 0.2, 0.25, "Days to weeks\nLowest cost\nEmpty facility", COLORS["accent"]),
        ("Warm Site", 0.5, 0.50, "Hours to a day\nModerate cost\nPartial equipment", COLORS["warning"]),
        ("Hot Site", 0.8, 0.80, "Minutes to hours\nHighest cost\nFull mirror", COLORS["danger"]),
    ]

    # Background gradient effect
    for i in range(100):
        x = i / 100
        ax.axvline(x, color=plt.cm.RdYlGn_r(x * 0.8), alpha=0.05, linewidth=5)

    for label, x, y, desc, color in sites:
        draw_box(ax, x, y, 0.18, 0.15, f"{label}\n\n{desc}", color, fontsize=7)

    # Axes labels
    ax.text(0.5, 0.02, "Cost  →", ha="center", fontsize=11, fontweight="bold", color=COLORS["text"])
    ax.text(0.02, 0.5, "Recovery\nSpeed  →", ha="center", va="center", fontsize=10,
            fontweight="bold", color=COLORS["text"], rotation=90)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.savefig(OUTPUT_DIR / "dr-recovery-sites.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print("  Generated: dr-recovery-sites.png")


# ── Main ──────────────────────────────────────────────────────────

def main():
    print("NOSS IT-020 Illustration Generator")
    print(f"Output: {OUTPUT_DIR}\n")

    gen_network_topologies()
    gen_raid_levels()
    gen_troubleshooting_flowchart()
    gen_server_rack()
    gen_security_zones()
    gen_asset_lifecycle()
    gen_cable_wiring()
    gen_maintenance_schedule()
    gen_osi_model()
    gen_project_lifecycle()
    gen_dr_strategy()

    pngs = list(OUTPUT_DIR.glob("*.png"))
    print(f"\nGenerated {len(pngs)} illustrations:")
    for p in sorted(pngs):
        print(f"  {p.name} ({p.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
