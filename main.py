from src.orchestrator import TestOrchestrator
from src.report_generator import ReportGenerator
from src.dashboard import Dashboard


def success_test():
    return "API Working"


def failure_test():
    raise Exception(
        "Expected status 200 but got 500"
    )


orchestrator = TestOrchestrator()

results = []

print("Running Success Test...")
success_result = orchestrator.execute_test(
    success_test
)

results.append(success_result)

print(success_result)

print("\nRunning Failure Test...")
failure_result = orchestrator.execute_test(
    failure_test
)

results.append(failure_result)

print(failure_result)


passed = len(
    [r for r in results if r["status"] == "passed"]
)

failed = len(
    [r for r in results if r["status"] == "failed"]
)

stats = {
    "total_tests": len(results),
    "passed": passed,
    "failed": failed,
    "pass_percentage":
        round((passed / len(results)) * 100, 2)
}


report_generator = ReportGenerator()

report_generator.generate_json_report(
    {
        "results": results,
        "stats": stats
    }
)

report_generator.generate_html_report(
    {
        "results": results,
        "stats": stats
    }
)

Dashboard.generate_html_dashboard(
    stats
)

print("\nReports Generated")
print("reports/json/report.json")
print("reports/html/report.html")
print("reports/html/dashboard.html")