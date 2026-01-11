from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import from_json, col, to_json, struct

from common.config import (
  BOOTSTRAP_SERVERS,
  PRODUCER_TOPIC,
  CONSUMER_TOPIC,
  CHECKPOINT_PATH
) 

from common.schema import DIABETES_SCHEMA


def read_kafka_stream(spark:SparkSession) -> DataFrame:
  return spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", BOOTSTRAP_SERVERS) \
    .option("subscribe", PRODUCER_TOPIC) \
    .option("startingOffsets", "earliest") \
    .load()


def parse_json(stream_df: DataFrame) -> DataFrame:
  return stream_df \
    .selectExpr("CAST(value as STRING)") \
    .select(from_json(col("value"), DIABETES_SCHEMA).alias("data")) \
    .select("data.*")


def write_stream(
  df: DataFrame
):
  return df \
    .select(to_json(struct("*")).alias("value")) \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", BOOTSTRAP_SERVERS) \
    .option("topic", CONSUMER_TOPIC) \
    .option("checkpointLocation", CHECKPOINT_PATH) \
    .start()
