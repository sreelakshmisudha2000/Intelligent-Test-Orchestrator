# Intelligent System Verification & Test Orchestration Platform

## Overview

An automation-focused testing platform developed using Python that enables API testing, file validation, failure classification, AI-assisted failure analysis, test orchestration, report generation, and dashboard monitoring.

The platform helps automate verification processes by executing tests, classifying failures, generating recommendations, and producing execution reports.

---

## Features

### Test Orchestration

* Execute automated test workflows
* Manage test execution lifecycle
* Capture execution results

### API Testing

* GET request validation
* Response status verification
* Timeout handling
* Environment failure detection

### File Validation

* CSV validation
* JSON validation
* Excel validation
* Schema and structure checks

### Failure Classification

* API Failure
* Validation Failure
* Timeout Failure
* Environment Failure

### AI-Assisted Failure Analysis

* Root cause suggestions
* Failure categorization
* Recommended remediation actions

### Reporting

* HTML Report Generation
* JSON Report Generation

### Dashboard

* Total Tests Executed
* Passed Tests
* Failed Tests
* Pass Percentage Metrics

---

## Technology Stack

* Python 3.11
* SQLite
* Requests
* Pandas
* OpenPyXL
* Pytest
* Git & GitHub

---

## Project Structure

```text
Intelligent-Test-Orchestrator/
│
├── src/
│   ├── database.py
│   ├── api_tests.py
│   ├── file_validation.py
│   ├── failure_classifier.py
│   ├── ai_failure_analyzer.py
│   ├── report_generator.py
│   ├── dashboard.py
│   └── orchestrator.py
│
├── tests/
│   └── test_api.py
│
├── reports/
│   ├── html/
│   └── json/
│
├── sample_files/
├── requirements.txt
├── README.md
└── main.py
```

---

## Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Run tests:

```bash
pytest
```

---

## Future Enhancements

* Historical test execution tracking
* Database-driven dashboard
* Test scheduling
* Flask-based web interface
* PostgreSQL integration
* Docker deployment

---

## Author

Sreelakshmi
