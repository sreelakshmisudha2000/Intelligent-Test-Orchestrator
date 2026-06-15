from src.failure_classifier import FailureClassifier
from src.ai_failure_analyzer import AIFailureAnalyzer


class TestOrchestrator:

    def execute_test(self, test_function):

        try:
            result = test_function()

            return {
                "status": "passed",
                "result": result
            }
        
        except Exception as e:

            failure_type = FailureClassifier.classify(e)

            ai_analysis = AIFailureAnalyzer.analyze(
                failure_type, 
                str(e)
            )

            return {
                "status": "failed",
                "failure_type": failure_type,
                "message": str(e),
                "ai_analysis": ai_analysis
            }