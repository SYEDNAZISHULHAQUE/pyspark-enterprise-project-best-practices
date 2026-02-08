from pyspark.sql.functions import *


# ============================
# Filter Salaries (Example)
# ============================
def filter_high_salary(salaries_df, min_salary=7000):
    """
    Keep employees with salary >= min_salary
    """
    return salaries_df.filter(col("monthly_salary") >= min_salary)


# ============================
# Join Employees & Salaries
# ============================
def join_employees_salaries(employees_df, salaries_df):

    return employees_df.join(
        salaries_df,
        on="emp_id",
        how="inner"
    )


# ============================
# Aggregate by State
# ============================
def aggregate_salary_by_state(joined_df):

    return (
        joined_df
        .groupBy("state")
        .agg(
            count("emp_id").alias("employee_count"),
            sum("monthly_salary").alias("total_salary"),
            avg("monthly_salary").alias("avg_salary"),
            sum("bonus").alias("total_bonus")
        )
    )
