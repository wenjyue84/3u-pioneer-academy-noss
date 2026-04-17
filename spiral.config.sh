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
SPIRAL_FOCUS="Enhance Tuinalogy (推拿疗法 MP-031-3:2016) Chinese WIM materials in tuinalogy-services/ across all 7 CUs (C01-C05, E01, E02). Goals: (1) add appropriate image placeholders with markdown syntax + captions for meridian charts, technique illustrations, anatomy diagrams; (2) improve readability with subheadings, callouts, tables, mnemonic boxes; (3) humanize writing with clinical vignettes, instructor notes, reflection prompts, case studies; (4) apply educational theory — Bloom's taxonomy for learning objectives (记忆/理解/应用/分析/评价/创造), ARCS motivation model, scaffolding, spaced retrieval; (5) maintain Simplified Chinese (简体中文) throughout with bilingual EN/BM terms for clinical vocabulary; (6) preserve WIM headers and coding format MP-031-3:2016-[CU]/[DocCode]([seq]/[total]); (7) expand each document to ~5x the original NOSS source length with substantive content. Critical safety topics: pregnancy contraindications (禁忌五穴), TCM theory (经络/八纲/四诊), Malaysian regulations (T&CM Act 2013, OSHA 1994, PDPA 2010, MOH Code of Ethics 2007)."
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
