import pytest
from conftest import spark
from lib.utils import get_spark_session
from lib.Data_reader import read_employees, read_salaries


@pytest.mark.transformation()
def test_emp_reader(spark):
    count_emp = read_employees(spark, "LOCAL").count()
    assert count_emp == 50

def test_salary_reader():
    count_salary = read_salaries(spark, "LOCAL").count()
    assert count_salary == 50