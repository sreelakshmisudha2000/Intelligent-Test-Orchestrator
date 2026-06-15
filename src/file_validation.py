import csv
import json
import pandas as pd


class ValidationFailure(Exception):
    def __init__(self, failure_type, message):
        self.failure_type = failure_type
        self.message = message
        super().__init__(message)


class FileValidator:
    def validate_csv(
            self,
            file_path, 
            required_headers=None,
            expected_rows=None
    ):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)

                headers = next(reader)
                rows = list(reader)

            if required_headers:
                for header in required_headers:
                    if header not in header:
                        raise ValidationFailure(
                            "validation", 
                            f"Missing header: {header}"
                        )
            
            if expected_rows is not None:
                if len(rows) != expected_rows:
                    raise ValidationFailure(
                        "validation",
                        f"Expected {expected_rows} rows, found {len(rows)}"
                    )
            return {
                "status" : "passed",
                "headers" : headers,
                "row_count" : len(rows)
            }
        
        except ValidationFailure:
            raise

        except Exception as e:
            raise ValidationFailure(
                "environment",
                str(e)
            )

    def validate_json(
            self,
            file_path,
            required_fields=None
    ):
        try:
            with open(file_path, "r", encoidng="utf-8") as file:
                data = json.load(file)

            if required_fields:
                for field in required_fields:
                    if field not in data:
                        raise ValidationFailure(
                            "validation", 
                            f"Missing field: {field}"
                        )
        
            return {
                "status" : "passed",
                "data" : data,
            }
         
        except json.JSONDecodeError:
            raise ValidationFailure(
                "validation",
                "Invalid JSON format"
            )

        except Exception as e:
            raise ValidationFailure(
                "environment",
                str(e)
            )
        
    def validate_excel(
            self,
            file_path,
            required_columns=None
    ):
        try:
            df = pd.read_excel(file_path)

            if required_columns:
                for column in required_columns:
                    if column not in df.columns:
                        raise ValidationFailure(
                            "validation", 
                            f"Missing column: {column}"
                        )
        
            return {
                "status" : "passed",
                "columns" : list(df.columns),
                "row_count" : len(df),
            }
         
        except ValidationFailure:
            raise 
        
        except Exception as e:
            raise ValidationFailure(
                "environment",
                str(e)
            )