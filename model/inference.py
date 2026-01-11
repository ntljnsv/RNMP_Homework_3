from pyspark.ml import PipelineModel
from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from common.config import MODEL_PATH
from common.config import FEATURE_COLS


def load_model():
  return PipelineModel.load(MODEL_PATH)


def run_inference(
  model: PipelineModel,
  df: DataFrame
) -> DataFrame:
  predictions = model.transform(df)
  output = predictions.select(
    *FEATURE_COLS,
    col("prediction").cast("int").alias("predicted_diabetes")
  )

  return output
