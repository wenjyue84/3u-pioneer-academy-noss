#!/usr/bin/env bash
# spiral.config.sh — NOSS to WIM Enhancement

# No test command — this is a content project, not software
SPIRAL_VALIDATE_CMD="echo 'Content review pass'"
SPIRAL_REPORTS_DIR="test-reports"

# Loop control
MAX_SPIRAL_ITERS=99
TIME_LIMIT_MINS=0
SPIRAL_RALPH_ITERS=120
SPIRAL_GATE_MODE=proceed

# Model routing — use sonnet for content quality
SPIRAL_MODEL_ROUTING=sonnet
SPIRAL_THINKING_EFFORT=high

# Skip research — we already have all source material
# SPIRAL_FOCUS="WIM content enhancement for BEV and Aesthetic subjects"

# Cost controls
SPIRAL_STORY_COST_HARD_USD=10.00
SPIRAL_STORY_COST_WARN_USD=5.00
SPIRAL_COST_CEILING=100.00

# Memory
SPIRAL_MEMORY_WATCHDOG=0
SPIRAL_WORKER_MEMORY_LIMIT=1024

# Content project — skip enrichment and security
SPIRAL_STORY_ENRICHMENT=false
SPIRAL_SECURITY_SCAN=false
SPIRAL_SKIP_ADR=true
SPIRAL_SKIP_SELF_REVIEW=false

# Capacity
SPIRAL_CAPACITY_LIMIT=50
SPIRAL_MAX_AI_SUGGEST=3

# Missing vars that spiral.sh expects
SPIRAL_AUTO_ARCHIVE_THRESHOLD=0
SPIRAL_ZERO_PROGRESS_LIMIT=0
SPIRAL_CASCADE_FAN_OUT_LIMIT=5
SPIRAL_CONSECUTIVE_FAIL_ABORT=0
