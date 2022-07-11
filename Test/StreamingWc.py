from pyspark.sql import SparkSession
import lib.logger import Log4j
if __name__ == '__main__':
    spark = SparkSession\
        .builder\
        .appName("Streaming Word Count")\
        .master('local[3]')\
        .getOrCreate()

    logger = Log4J(spark)

    # 1. read a streaming source - input dataframe
    lines_df = spark.readStream.format('socket').option('host', 'localhost').option('port','9999').load()

    # 2.
    lines_df.printSchema()
