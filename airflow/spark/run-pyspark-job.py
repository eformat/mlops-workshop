import os
from pyspark.sql import SparkSession
import spark_util

def init_spark():
    spark = spark_util.getOrCreateSparkSession("Hello from Python file")
    sc = spark.sparkContext
    return spark, sc

def main():
    spark,sc = init_spark()
    nums = sc.parallelize([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    print(nums.map(lambda x: x*x).collect())


if __name__ == '__main__':
    main()
