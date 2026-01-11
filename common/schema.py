from typing import List

from pyspark.sql.types import (
  StructType, StructField, IntegerType, DoubleType
)


DIABETES_SCHEMA: StructType = StructType([
  StructField("HighBP", IntegerType()),
  StructField("HighChol", IntegerType()),
  StructField("CholCheck", IntegerType()),
  StructField("BMI", DoubleType()),
  StructField("Smoker", IntegerType()),
  StructField("Stroke", IntegerType()),
  StructField("HeartDiseaseorAttack", IntegerType()),
  StructField("PhysActivity", IntegerType()),
  StructField("Fruits", IntegerType()),
  StructField("Veggies", IntegerType()),
  StructField("HvyAlcoholConsump", IntegerType()),
  StructField("AnyHealthcare", IntegerType()),
  StructField("NoDocbcCost", IntegerType()),
  StructField("GenHlth", IntegerType()),
  StructField("MentHlth", IntegerType()),
  StructField("PhysHlth", IntegerType()),
  StructField("DiffWalk", IntegerType()),
  StructField("Sex", IntegerType()),
  StructField("Age", IntegerType()),
  StructField("Education", IntegerType()),
  StructField("Income", IntegerType())
])

INT_COLS: List[str] = [
  "HighBP", "HighChol", "CholCheck", "Smoker", "Stroke",
  "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
  "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost",
  "GenHlth", "MentHlth", "PhysHlth", "DiffWalk",
  "Sex", "Age", "Education", "Income"
]

DOUBLE_COLS: List[str] = ["BMI"]
