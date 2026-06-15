import requests

class APIFailure(Exception):
    def __init__(self, failure_type, message):
        self.failure_type = failure_type
        self.message = message
        super().__init__(message)

class APITester:

    def execute_get(
            self,
            url,
            expected_status=200,
            timeout=30
    ):
        try:
            response = requests.get(
                url,
                timeout=timeout
            )

            if response.status_code != expected_status:
                raise APIFailure(
                    "api",
                    f"Expected {expected_status}, got {response.status_code}"
                )
            
            return {
                "status": "passed",
                "response": response.json()
            }
        
        except requests.Timeout:
            raise APIFailure(
                "timeout",
                "Request timed out"
            )
        
        except requests.ConnectionError:
            raise APIFailure(
                "environment",
                "Unable to connect to server"
            )
        

    def execute_post(
            self,
            url,
            payload,
            expected_status=201,
            timeout=30
    ):
        try:
            response = requests.post(
                url,
                json=payload,
                timeout=timeout
            )

            if response.status_code != expected_status:
                raise APIFailure(
                    "api",
                    f"Expected {expected_status}, got {response.status_code}"
                )
            
            return {
                "status": "passed",
                "response": response.json()
            }
        
        except requests.Timeout:
            raise APIFailure(
                "timeout",
                "Request timed out"
            )
        
        except requests.ConnectionError:
            raise APIFailure(
                "environment",
                "Unable to connect to server"
            )
        
