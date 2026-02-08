# 🚀 # PySpark Best Practices Project

This repository demonstrates a production-style PySpark ETL project
following real-world data engineering best practices.

It is designed for learning, practice, and professional portfolio use.

---

## Project Objectives

This project helps you:

- Build scalable PySpark pipelines
- Follow industry-standard folder structure
- Use configuration-driven ingestion
- Separate business logic from orchestration
- Apply version control with Git and GitHub
- Prepare for data engineering interviews

---

## Project Structure

The project follows this structure:

pyspark_best_practices/

    application_main.py

    configs/
        application.conf
        pyspark.conf

    data/
        employees_demo.csv
        salaries_demo.csv

    lib/
        __init__.py
        config_reader.py
        Data_reader.py
        Data_Manipulation.py
        utils.py

    Pipfile
    Pipfile.lock
    README.md

---

## Architecture Overview

This project follows a layered architecture:

1. Configuration Layer  
   Handles environment-specific parameters and file paths.

2. Ingestion Layer  
   Reads data from external sources using predefined schemas.

3. Transformation Layer  
   Applies business rules, joins, and aggregations.

4. Orchestration Layer  
   Controls pipeline execution through application_main.py.

5. Utility Layer  
   Manages Spark session and shared functions.

---

## Data Description

This project uses two demo datasets.

Employees Dataset

- emp_id
- emp_name
- state
- department
- experience_years

Salaries Dataset

- salary_id
- emp_id
- monthly_salary
- bonus
- pay_month

The datasets are joined using emp_id.

---

## How to Run the Project

Step 1: Activate virtual environment

pipenv shell

or

source venv/bin/activate

Step 2: Run the application

python application_main.py dev

Replace dev with test or prod as needed.

---

## Configuration Management

All configurations are stored in:

configs/application.conf

Example:

employees.file.path=data/employees_demo.csv
salaries.file.path=data/salaries_demo.csv

spark.app.name=PySparkBestPractices

This allows environment-based execution.

---

## Development Workflow

Recommended daily workflow:

1. Pull latest changes

   git pull

2. Make code changes

3. Check status

   git status

4. Add files

   git add .

5. Commit changes

   git commit -m "Meaningful message"

6. Push to GitHub

   git push

---

## Coding Best Practices

This project follows:

- Modular code design
- Reusable functions
- Clear naming conventions
- Config-driven pipelines
- Separation of concerns
- Version-controlled development

---

## Testing Guidelines

Before committing code:

- Run the application locally
- Validate input schemas
- Verify join and aggregation results
- Check logs and outputs

---

## Future Enhancements

Possible improvements:

- Add logging framework
- Add unit testing
- Add CI/CD pipeline
- Add cloud storage integration
- Add Airflow orchestration
- Add Delta Lake support

---

## Author

Maintained by: Syed Nazishul Haque

This repository is part of a professional learning portfolio.
