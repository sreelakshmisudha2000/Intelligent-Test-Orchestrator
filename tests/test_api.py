from src.ai_failure_analyzer import AIFailureAnalyzer


def test_ai_analysis():

    result = AIFailureAnalyzer.analyze(
        "api",
        "Expected status 200 but got 500"
    )

    assert result["failure_type"] == "api"