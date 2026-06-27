# Study Buddy-AI

A secure multi-step AI agent for structured exam planning built using Google ADK.

Overview:
StudyBuddy AI helps students generate structured and personalized study plans for exam preparation. It takes raw user input and converts it into a clear, step-by-step study strategy.

Key Features:
- Multi-step AI workflow architecture
- Security layer for prompt injection detection
- PII redaction for safe input handling
- Structured study plan generation
- Deterministic and consistent outputs

Architecture:
1. Security Node → filters unsafe or malicious inputs  
2. Planner Node → generates structured study plan  
3. Motivation Node → adds reinforcement and encouragement  
4. Orchestrator → controls workflow execution

Safety Design:
- Detects prompt injection attempts
- Redacts sensitive information (PII)
- Blocks unsafe queries before processing

Goal:
To demonstrate how AI agents can be designed with structured workflows, safety controls, and reliable outputs for real-world educational use cases.
