#!/usr/bin/env bash
# spiral.config.sh — NOSS to WIM Enhancement (Content Project)

# Validation — content project, no real test suite
SPIRAL_VALIDATE_CMD="echo 'Content review pass'"
SPIRAL_REPORTS_DIR="test-reports"

# Loop control — CONTINUOUS MODE
MAX_SPIRAL_ITERS=999
SPIRAL_RALPH_ITERS=120
SPIRAL_GATE_MODE=proceed
SPIRAL_CONTINUOUS=true
SPIRAL_CONTINUOUS_COOLDOWN_SECS=30

# Model routing
SPIRAL_MODEL_ROUTING=sonnet
SPIRAL_THINKING_EFFORT=high

# Research — ENABLED, focused on content improvement
SPIRAL_FOCUS="Enhance WIM (Written Instructional Materials) document quality: format compliance with Buku Panduan WIM Edisi 2020 (header boxes, TAJUK/TUJUAN/PENERANGAN structure, BAHAGIAN sections for KT, LANGKAH KERJA tables for KK, 4-phase lesson plans for PM, SENARAI SEMAK checklists), technical content accuracy, bilingual EN/BM terminology, assessment rubrics, and full coverage of NOSS CoCU work activities. Subjects: BEV automotive (G452-010-3:2023), Aesthetic Services (S960-002-3:2020), IT Computer System (IT-020-3/4/5:2013)."
SPIRAL_RESEARCH_MODEL=sonnet
SPIRAL_RESEARCH_TIMEOUT=600

# Story discovery — HIGH VOLUME
SPIRAL_MAX_AI_SUGGEST=15
SPIRAL_AI_SUGGEST_MIN_SCORE=0
SPIRAL_MAX_RESEARCH_STORIES=10

# Story validation — RELAXED for content projects
SPIRAL_STORY_VALIDATE_MIN_OVERLAP=0
SPIRAL_SEMANTIC_DEDUP_THRESHOLD=0.92
SPIRAL_VALIDATION_VOTES=1

# Content project — large diffs expected
SPIRAL_MAX_DIFF_LINES=10000
SPIRAL_MAX_FILES_PER_STORY=60
SPIRAL_SCOPE_CREEP_ACTION=warn

# Cost controls — generous for long runs
SPIRAL_STORY_COST_HARD_USD=15.00
SPIRAL_STORY_COST_WARN_USD=8.00
SPIRAL_COST_CEILING=500.00

# Timeouts — content stories need time
SPIRAL_STORY_TIMEOUT_SMALL=900
SPIRAL_STORY_TIMEOUT_MEDIUM=1800
SPIRAL_STORY_TIMEOUT_LARGE=3600
SPIRAL_IMPL_TIMEOUT=3600
SPIRAL_WORKER_TIMEOUT=3600

# Memory — Windows safe defaults
SPIRAL_MEMORY_WATCHDOG=0
SPIRAL_WORKER_MEMORY_LIMIT=1024

# Skip features not relevant to content projects
SPIRAL_STORY_ENRICHMENT=false
SPIRAL_SECURITY_SCAN=false
SPIRAL_SKIP_ADR=true
SPIRAL_SKIP_SELF_REVIEW=false

# Capacity
SPIRAL_CAPACITY_LIMIT=100
SPIRAL_MAX_PENDING=50

# Stability
SPIRAL_AUTO_ARCHIVE_THRESHOLD=0
SPIRAL_ZERO_PROGRESS_LIMIT=0
SPIRAL_CASCADE_FAN_OUT_LIMIT=10
SPIRAL_CONSECUTIVE_FAIL_ABORT=0
