class Dashboard:

    @staticmethod
    def generate_html_dashboard(
        stats,
        file_name="reports/html/dashboard.html"
    ):

        html = f"""
        <html>
        <head>
            <title>Test Dashboard</title>
            <style>
                body {{
                    font-family: Arial;
                    margin: 40px;
                }}

                .card {{
                    border: 1px solid #ddd;
                    padding: 20px;
                    margin: 10px;
                    border-radius: 8px;
                }}

                .passed {{
                    color: green;
                }}

                .failed {{
                    color: red;
                }}
            </style>
        </head>

        <body>

        <h1>Test Execution Dashboard</h1>

        <div class="card">
            <h2>Total Tests</h2>
            <h3>{stats['total_tests']}</h3>
        </div>

        <div class="card passed">
            <h2>Passed</h2>
            <h3>{stats['passed']}</h3>
        </div>

        <div class="card failed">
            <h2>Failed</h2>
            <h3>{stats['failed']}</h3>
        </div>

        <div class="card">
            <h2>Pass Percentage</h2>
            <h3>{stats['pass_percentage']}%</h3>
        </div>

        </body>
        </html>
        """

        with open(file_name, "w") as file:
            file.write(html)

        return file_name