# 🚀 PySpark Enterprise ETL Project – Best Practices

This repository demonstrates a production-style PySpark ETL project built using real-world data engineering best practices.

It is designed for:
- Learning PySpark the right way
- Practicing enterprise-grade ETL design
- Showcasing a professional portfolio project
- Preparing for Data Engineer interviews

---

## 🎯 Project Objectives

This project helps you learn how to:

- Build scalable PySpark ETL pipelines
- Follow industry-standard project structure
- Use configuration-driven ingestion
- Separate orchestration, ingestion, and transformation logic
- Implement logging for debugging and monitoring
- Write unit tests using pytest
- Use Git and GitHub like a professional data engineer

---

## 📁 Project Structure

Project layout:

pyspark_best_practices/

application_main.py  
Main entry point that orchestrates the ETL flow

configs/  
Contains application and Spark configuration files

data/  
Demo input datasets used for local execution

lib/  
Reusable modules for configuration, ingestion, transformation, and utilities

tests/  
Unit tests written using pytest

Pipfile  
Pipfile.lock  
Dependency management files

README.md  
Project documentation

---

## 🏗 Architecture Overview

This project follows a layered architecture:

1. Configuration Layer  
   Manages environment-specific settings and file paths

2. Ingestion Layer  
   Reads input data using predefined schemas

3. Transformation Layer  
   Applies business logic such as joins and aggregations

4. Orchestration Layer  
   Controls pipeline execution using application_main.py

5. Utility Layer  
   Creates Spark session and shared helper functions

---

## 📊 Data Description

This project uses two demo datasets.

Employees dataset fields:
- emp_id
- emp_name
- state
- department
- experience_years

Salaries dataset fields:
- salary_id
- emp_id
- monthly_salary
- bonus
- pay_month

The datasets are joined using emp_id.

---

## ▶️ How to Run the Project

Step 1: Create and activate virtual environment

Using pipenv:
pipenv shell

Or using venv:
source venv/bin/activate

Step 2: Run the application

python application_main.py LOCAL

You can replace LOCAL with DEV, TEST, or PROD if configurations are added.

---

## ⚙️ Configuration Management

All configurations are stored in:

configs/application.conf

Example configuration:

employees.file.path=data/employees_demo.csv  
salaries.file.path=data/salaries_demo.csv  
spark.app.name=PySparkBestPractices  

This makes the application environment-independent and easy to scale.

---

## 🪵 Logging Framework

This project uses Python logging integrated with Spark.

Logging benefits:
- Tracks pipeline execution
- Helps debug data issues
- Provides production-level observability

Logs typically include:
- Application start and end
- Data ingestion status
- Transformation completion
- Error and exception details

You can extend logging to write logs to files or centralized systems.

---

## 🧪 Unit Testing with Pytest

This project supports unit testing using pytest.

Testing approach:
- Validate data ingestion logic
- Test transformation functions independently
- Use Spark session fixtures via pytest

Run tests using:

pytest tests/

This ensures code quality and makes refactoring safer.

---

## ✅ Coding Best Practices Followed

- Modular and reusable code
- Clear naming conventions
- Config-driven pipelines
- Separation of concerns
- Logging and testability
- Production-style project layout

---

## 🚀 Future Enhancements

Planned improvements:
- Add CI/CD pipeline
- Add Airflow orchestration
- Add cloud storage integration (S3, ADLS)
- Add Delta Lake support
- Add data quality checks
- Add Docker support

---

## 👤 Author

Maintained by: Syed Nazishul Haque

This repository is part of a professional data engineering learning portfolio.
