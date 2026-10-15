# AI-Assisted QA & Model Context Protocol (MCP) Testing Server

[![MCP Standard](https://img.shields.io/badge/Model_Context_Protocol-v1.0-purple.svg)](https://modelcontextprotocol.io/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)

An innovative **Model Context Protocol (MCP)** server built in **Python** to empower AI coding assistants (like Antigravity / Claude) with specialized software testing tools:
- Automated Test Case Generation from API specifications.
- Error Log Analysis & Root Cause Triage.
- Automated Jira Bug Draft Formatting.

Developed by **[Aishwarya Shanmugam](https://linkedin.com/in/aishwaryyaa12)** (QA Engineer).

---

## 🚀 Overview

The Model Context Protocol (MCP) is an open standard that connects AI models to external tools and context sources. This server provides specialized tools for QA Engineers:

1. `generate_test_cases(endpoint, method)`: Returns boundary, edge-case, and happy-path test scenarios.
2. `analyze_stack_trace(trace_text)`: Identifies root causes and categorizes failure types.
3. `format_jira_issue(summary, description, expected, actual)`: Formats clean markdown/Jira issues.

---

## 🛠️ Installation & Usage

```bash
git clone https://github.com/aishwaryyaa12/ai-mcp-test-assistant.git
cd ai-mcp-test-assistant

pip install -r requirements.txt
python mcp_server.py
```

---

## 👩‍💻 Author
**Aishwarya Shanmugam** — QA Engineer | Test Automation Specialist  
📍 Steinenbronn (Stuttgart Region), Germany  
🔗 [LinkedIn Profile](https://linkedin.com/in/aishwaryyaa12)
