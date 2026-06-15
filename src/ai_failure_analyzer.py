class AIFailureAnalyzer:

    @staticmethod
    def analyze(failure_type, message):

        analysis = {
            "failure_type": failure_type,
            "original_message": message
        }

        if failure_type == "api":
            analysis["possible_causes"] = [
                "Incorrect API endpoint",
                "Unexpected response status",
                "Backend service issue"
            ]

            analysis["recommendation"] = (
                "Verify endpoint URL, request payload, "
                "and backend service availability."
            )

        elif failure_type == "validation":
            analysis["possible_causes"] = [
                "Invalid file structure",
                "Missing required fields",
                "Schema mismatch"
            ]

            analysis["recommendation"] = (
                "Review file schema and validate required fields."
            )

        elif failure_type == "timeout":
            analysis["possible_causes"] = [
                "Slow server response",
                "Network latency",
                "Large payload processing"
            ]

            analysis["recommendation"] = (
                "Increase timeout and inspect server performance."
            )

        else:
            analysis["possible_causes"] = [
                "Connection problem",
                "System configuration issue",
                "Unexpected runtime error"
            ]

            analysis["recommendation"] = (
                "Inspect logs and verify environment configuration."
            )

        return analysis