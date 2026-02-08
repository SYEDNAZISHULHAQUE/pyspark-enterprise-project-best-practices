import sys
from lib import utils, Data_Manipulation, Data_reader
from pyspark.sql.functions import *
import lib.utils
print("UTILS FILE:", lib.utils.__file__)
print("ATTRS:", dir(lib.utils))

if __name__ == "__main__":

    # ============================
    # Validate Environment
    # ============================
    if len(sys.argv) < 2:
        print("Please specify the environment")
        sys.exit(-1)

    job_run_env = sys.argv[1]

    print("Creating Spark Session...")
    spark = utils.get_spark_session(job_run_env)
    print("Spark Session Created")


    # ============================
    # Read Input Data
    # ============================
    print("Reading Employees Data...")
    employees_df = Data_reader.read_employees(spark, job_run_env)

    print("Reading Salaries Data...")
    salaries_df = Data_reader.read_salaries(spark, job_run_env)


    # ============================
    # Transformations
    # ============================
    print("Filtering High Salary Records...")
    salaries_filtered = Data_Manipulation.filter_high_salary(
        salaries_df,
        min_salary=7000
    )

    print("Joining Employees and Salaries...")
    joined_df = Data_Manipulation.join_employees_salaries(
        employees_df,
        salaries_filtered
    )

    print("Aggregating Salary By State...")
    aggregated_results = Data_Manipulation.aggregate_salary_by_state(
        joined_df
    )


    # ============================
    # Output
    # ============================
    print("Final Aggregated Results:")
    aggregated_results.show(truncate=False)

    print("End of Main Job")
