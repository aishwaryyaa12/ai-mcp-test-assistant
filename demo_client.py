"""
Interactive Demo Script for AI-MCP Test Assistant
Demonstrates how AI agent workflows invoke the MCP server tools directly.
"""

from mcp_server import generate_api_test_scenarios, format_jira_bug

def run_demo():
    print("=" * 65)
    print("AI-MCP TEST ASSISTANT: DEMONSTRATING TOOL INVOCATIONS")
    print("=" * 65)
    
    print("\n--- 1. Invoking generate_api_test_scenarios ---")
    scenarios = generate_api_test_scenarios(
        endpoint="/api/v1/orders/checkout",
        http_method="POST",
        auth_required=True
    )
    print(scenarios)
    
    print("\n--- 2. Invoking format_jira_bug ---")
    bug = format_jira_bug(
        summary="Checkout API returns 500 when discount code contains unicode characters",
        expected_result="API returns 400 Bad Request with error: 'Invalid discount code format'",
        actual_result="API returns 500 Internal Server Error with unhandled ValueError exception",
        repro_steps="Add product ID 101 to cart\nApply discount code 'HERBST-2026-🏷️'\nClick Complete Checkout",
        severity="High",
        environment="Staging v2.5.0"
    )
    print(bug)
    
    print("=" * 65)
    print("DEMO COMPLETE: ALL MCP TOOLS EXECUTED SUCCESSFULLY")
    print("=" * 65)

if __name__ == "__main__":
    run_demo()
