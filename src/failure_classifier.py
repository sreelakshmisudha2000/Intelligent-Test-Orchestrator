class FailureClassifier:

    @staticmethod
    def classify(exception):

        error_text = str(exception).lower()

        if "timeout" in error_text:
            return "timeout"
        
        if "status" in error_text:
            return "api"
        
        if "missing" in error_text:
            return "validation"
        
        return "environment"