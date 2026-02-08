from lib.config_reader import get_app_config


# =========================
# Employees Schema
# =========================
def get_employees_schema():
    schema = """
        emp_id int,
        emp_name string,
        state string,
        department string,
        experience_years int
    """
    return schema


# =========================
# Read Employees
# =========================
def read_employees(spark, env):

    conf = get_app_config(env)
    employees_file_path = conf["employees.file.path"]

    return (
        spark.read
        .format("csv")
        .option("header", "true")
        .schema(get_employees_schema())
        .load(employees_file_path)
    )


# =========================
# Salaries Schema
# =========================
def get_salaries_schema():
    schema = """
        salary_id int,
        emp_id int,
        monthly_salary int,
        bonus int,
        pay_month string
    """
    return schema


# =========================
# Read Salaries
# =========================
def read_salaries(spark, env):

    conf = get_app_config(env)
    salaries_file_path = conf["salaries.file.path"]

    return (
        spark.read
        .format("csv")
        .option("header", "true")
        .schema(get_salaries_schema())
        .load(salaries_file_path)
    )
