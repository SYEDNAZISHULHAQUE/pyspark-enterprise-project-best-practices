import sys
from lib import utils, Data_Manipulation, Data_reader
from pyspark.sql.functions import *
import lib.utils
from logger import Log4j

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
    logger = Log4j(spark)
    logger.warn("Created Spark Session")


    # ============================
    # Read Input Data
    # ============================
    logger.info("Reading Employees Data...")
    employees_df = Data_reader.read_employees(spark, job_run_env)

    logger.info("Reading Salaries Data...")
    salaries_df = Data_reader.read_salaries(spark, job_run_env)


    # ============================
    # Transformations
    # ============================
    logger.info("Filtering High Salary Records...")
    salaries_filtered = Data_Manipulation.filter_high_salary(
        salaries_df,
        min_salary=7000
    )

    logger.info("Joining Employees and Salaries...")
    joined_df = Data_Manipulation.join_employees_salaries(
        employees_df,
        salaries_filtered
    )

    logger.info("Aggregating Salary By State...")
    aggregated_results = Data_Manipulation.aggregate_salary_by_state(
        joined_df
    )


    # ============================
    # Output
    # ============================
    logger.info("Final Aggregated Results:")
    aggregated_results.show(truncate=False)

    logger.info("this is the end of main")
