#!/usr/bin/env bash
# spiral.config.sh — NOSS IT-020 Textbook Project

# Test command: gap analysis + docx generation
SPIRAL_VALIDATE_CMD="uv run scripts/gap_analysis.py && uv run --with python-docx scripts/generate_docx.py"
SPIRAL_REPORTS_DIR="test-reports"

# Story settings
SPIRAL_STORY_PREFIX="US"

# Loop control
MAX_SPIRAL_ITERS=9999
TIME_LIMIT_MINS=720
SPIRAL_RALPH_ITERS=120
SPIRAL_GATE_MODE="proceed"

# Model routing — auto escalation (haiku → sonnet → opus)
SPIRAL_MODEL_ROUTING="auto"
SPIRAL_THINKING_EFFORT="high"

# Capacity
SPIRAL_CAPACITY_LIMIT=50
SPIRAL_MAX_PENDING=30

# Cost control
SPIRAL_STORY_COST_HARD_USD=10.00
SPIRAL_STORY_COST_WARN_USD=5.00
SPIRAL_COST_CEILING=50.00

# Memory (Windows safe)
SPIRAL_MEMORY_WATCHDOG=0
SPIRAL_WORKER_MEMORY_LIMIT=1024
SPIRAL_LOW_POWER_MODE=1

# Story enrichment off (saves memory)
SPIRAL_STORY_ENRICHMENT=false

# Research — broader focus to discover new enhancement stories
SPIRAL_FOCUS="NOSS textbook quality, content depth, technical accuracy, formatting, JPK compliance, learning outcomes, practical exercises, industry relevance, docx generator improvements"
SPIRAL_RESEARCH_TIMEOUT=300
SPIRAL_MAX_AI_SUGGEST=10

# Skip test synthesis (no test framework in this project)
SPIRAL_SKIP_TEST_SYNTHESIS=1

# Git
SPIRAL_GIT_AUTHOR="Spiral NOSS"
SPIRAL_GIT_EMAIL="spiral@3upioneer.academy"

# Timeouts per complexity
SPIRAL_STORY_TIMEOUT_SMALL=600
SPIRAL_STORY_TIMEOUT_MEDIUM=1200
SPIRAL_STORY_TIMEOUT_LARGE=1800

# Logging
SPIRAL_LOG_LEVEL=INFO
SPIRAL_OPEN_DASHBOARD=1
