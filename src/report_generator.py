import json
from datetime import datetime


class ReportGenerator:

    def generate_json_report(
        self,
        run_data,
        file_name="reports/json/report.json"
    ):

        with open(file_name, "w") as file:
            json.dump(
                run_data,
                file,
                indent=4
            )

        return file_name

    def generate_html_report(
        self,
        run_data,
        file_name="reports/html/report.html"
    ):

        html = f"""
        <html>
        <head>
            <title>Test Report</title>
        </head>
        <body>

        <h1>Test Execution Report</h1>

        <p>
        Generated:
        {datetime.now()}
        </p>

        <h2>Result</h2>

        <pre>
        {json.dumps(run_data, indent=4)}
        </pre>

        </body>
        </html>
        """

        with open(file_name, "w") as file:
            file.write(html)

        return file_name