# LLM Input Safety Guardrail & Filter

A lightweight programmatic security layer designed to intercept, scan, and sanitize incoming text prompts before they reach Large Language Model (LLM) orchestration pipelines or live conversational AI agents.

## Features
- **Case-Insensitive Token Matching:** Normalizes input variations using lowercasing to prevent capitalization bypasses.
- **Dynamic Lexicon Ingestion:** Iterates cleanly through modular arrays of restricted target keywords using iterative loops.
- **Early-Exit Validation Routing:** Employs early return boolean logic to minimize pipeline latency on flagged inputs.

## Technical Details
The core module exposes `is_message_safe(message, banned_words)`, which returns boolean evaluations mapping directly into downstream conditional routing blocks.
