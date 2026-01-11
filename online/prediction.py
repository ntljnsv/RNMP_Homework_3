from pyspark.sql import SparkSession

from model.inference import load_model, run_inference
from online.kafka_io import read_kafka_stream, parse_json, write_stream


def create_spark() -> SparkSession:
  return SparkSession.builder \
  .appName("DiabetesHealthPrediction") \
  .master("local[*]") \
  .config(
    "spark.jars.packages",
    "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0"
  ) \
  .getOrCreate()


def main():
  spark = create_spark()

  raw_stream = read_kafka_stream(spark)
  parsed_stream = parse_json(raw_stream)

  model = load_model()

  output = run_inference(model, parsed_stream)

  query = write_stream(output)
  
  query.awaitTermination()


if __name__ == "__main__":
  main()
