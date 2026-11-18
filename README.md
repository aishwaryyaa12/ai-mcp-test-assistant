# AI-Powered Test Assistant (Model Context Protocol)

[![CI](https://github.com/aishwaryyaa12/ai-mcp-test-assistant/actions/workflows/ci.yml/badge.svg)](https://github.com/aishwaryyaa12/ai-mcp-test-assistant/actions)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-0.1+-009688?logo=fastapi&logoColor=white)](https://github.com/jlowin/fastmcp)
[![Pytest](https://img.shields.io/badge/Pytest-7.4+-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)

A specialized Model Context Protocol (MCP) server written in Python using FastMCP. It exposes deterministic Quality Engineering tools to AI assistants (such as Claude Desktop, Cursor, or custom agents) to automate API test scenario scaffolding and structured defect reporting.

**Author:** [Aishwarya Shanmugam](https://linkedin.com/in/aishwaryyaa12) (QA Automation Engineer)

---

## Why I Built This: Bridging AI Models with QA Tooling

Most teams currently use generative AI for QA in an ad-hoc way: engineers copy-paste Swagger specs or error logs into a web chat UI, resulting in generic suggestions and unformatted bug notes.

The **Model Context Protocol (MCP)** solves this by allowing local tools and scripts to connect directly to AI models via a standardized protocol. I built this server to solve two recurring bottlenecks:

1. **Deterministic Test Scenario Generation vs. LLM Hallucinations:**  
   When prompted casually, LLMs often overlook critical non-functional quadrants like idempotency, HTTP 413 payload limits, or role-based access control. The `generate_api_test_scenarios` tool enforces structured test quadrant coverage (Happy Path, Authentication/RBAC, Boundary/Negative Edge Cases, and Concurrency) with standardized naming conventions.

2. **Automating Defect Triage into Standardized Jira Markup:**  
   Raw stack traces from CI pipelines often lead to incomplete bug reports. The `format_jira_bug` tool takes raw error parameters and formats them into a production-grade Jira defect template with environment details, reproduction steps, and structured JSON logs.

3. **Dual-Layer Evaluation Principle:**  
   This project demonstrates a dual-layer approach to AI testing:
   * **Layer 1 (Deterministic Guardrails):** Enforced via Python type hints, Pydantic input models, and unit tests.
   * **Layer 2 (Semantic Layer):** The AI model provides contextual reasoning while staying bounded by structured tool inputs.

---

## Server Architecture & Tools

```text
├── .github/workflows/
│   └── ci.yml               # GitHub Actions CI running pytest and demo client
├── tests/
│   └── test_mcp_server.py   # Pytest unit tests validating tool inputs & formatting output
├── demo_client.py           # Standalone demonstration script showing programmatic invocations
├── mcp_server.py            # FastMCP server definition & registered tool functions
├── requirements.txt         # Project dependencies (fastmcp, pydantic, pytest)
└── README.md
```

### Exposed MCP Tools

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| `generate_api_test_scenarios` | `endpoint: str`, `http_method: str`, `auth_required: bool` | Generates a 4-quadrant test specification covering functional, security, boundary, and idempotency assertions. |
| `format_jira_bug` | `summary: str`, `expected_result: str`, `actual_result: str`, `repro_steps: str`, `severity: str`, `environment: str` | Formats raw test failure logs into an engineering-ready Jira defect ticket in Atlassian wiki markup. |

---

## Setup & Local Execution

### 1. Prerequisites
* Python 3.10+
* Git

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/aishwaryyaa12/ai-mcp-test-assistant.git
cd ai-mcp-test-assistant

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Unit Test Suite
```bash
pytest -v
```

### 4. Run the Interactive Demo Client
```bash
python demo_client.py
```

### 5. Running as an MCP Server (e.g. in Claude Desktop or IDEs)
```bash
# Start server via FastMCP CLI
fastmcp run mcp_server.py
```

To configure in `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "qa-test-assistant": {
      "command": "python",
      "args": ["/absolute/path/to/ai-mcp-test-assistant/mcp_server.py"]
    }
  }
}
```

---

## Continuous Integration (GitHub Actions)

On every `push` to `main`, `.github/workflows/ci.yml`:
1. Installs Python 3.11 and dependencies.
2. Runs the Pytest test suite (`tests/test_mcp_server.py`).
3. Executes `demo_client.py` to ensure tool output formatting remains stable across versions.
