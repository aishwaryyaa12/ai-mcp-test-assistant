from mcp.server.fastmcp import FastMCP

mcp = FastMCP("QA-Test-Assistant")

@mcp.tool()
def generate_api_test_scenarios(endpoint: str, http_method: str) -> str:
    """Generates comprehensive QA test scenarios for an API endpoint."""
    return f"""
QA Test Scenarios for {http_method.upper()} {endpoint}:
1. [Happy Path] Valid payload returns 200/201 with correct schema.
2. [Boundary] Maximum string lengths and numeric limits.
3. [Error Handling] Invalid auth token returns 401 Unauthorized.
4. [Edge Case] Empty/null body returns 400 Bad Request.
"""

@mcp.tool()
def format_jira_bug(summary: str, expected: str, actual: str) -> str:
    """Formats a bug report for Jira traceability."""
    return f"""
*Bug Summary*: {summary}
*Expected Result*: {expected}
*Actual Result*: {actual}
*Severity*: Medium/High
*Environment*: Staging / Chrome 120
"""

if __name__ == "__main__":
    mcp.run()
