import pytest
from mcp_server import generate_api_test_scenarios, format_jira_bug

def test_generate_api_scenarios_get():
    result = generate_api_test_scenarios("/api/v1/users", http_method="GET", auth_required=True)
    assert "### Test Specification for GET /api/v1/users" in result
    assert "HTTP 200/201" in result
    assert "HTTP 401 Unauthorized" in result
    assert "EDGE-01" in result

def test_generate_api_scenarios_public_post():
    result = generate_api_test_scenarios("/api/v1/auth/login", http_method="POST", auth_required=False)
    assert "### Test Specification for POST /api/v1/auth/login" in result
    assert "Public endpoint accessible" in result

def test_format_jira_bug():
    summary = "Cart total does not update after item quantity modification"
    expected = "Cart total re-aggregates accurately with discount applied"
    actual = "Cart total remains unchanged at previous value $120.00"
    repro = "Navigate to /cart\nClick '+' on item quantity\nVerify total price"
    
    report = format_jira_bug(
        summary=summary,
        expected_result=expected,
        actual_result=actual,
        repro_steps=repro,
        severity="Blocker",
        environment="Staging / Firefox"
    )
    
    assert "[BUG] Cart total does not update" in report
    assert "Blocker" in report
    assert "#1 Navigate to /cart" in report
    assert "#2 Click '+' on item quantity" in report
    assert "Cart total remains unchanged" in report
