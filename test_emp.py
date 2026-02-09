import pytest
from lib.utils import get_spark_session
from lib.Data_reader import read_employees, read_salaries

def test_emp_reader():
    spark = get_spark_session("LOCAL")
    count_emp = read_employees(spark, "LOCAL").count()
    assert count_emp == 50

def test_salary_reader():
    spark = get_spark_session("LOCAL")
    count_salary = read_salaries(spark, "LOCAL").count()
    assert count_salary == 50