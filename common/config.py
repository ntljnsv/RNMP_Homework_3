import os

from typing import List


TARGET_COL: str = "Diabetes_binary"

FEATURE_COLS: List[str] = [
  "HighBP", "HighChol", "CholCheck", "BMI", "Smoker", "Stroke",
  "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
  "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth",
  "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age", "Education", "Income"
]

PRODUCER_TOPIC: str = "diabetes_data"
CONSUMER_TOPIC:str = "diabetes_predictions"

ONLINE_DATA_PATH:str = "data/online.csv"
MODEL_PATH:str = "model/trained_model/"
CHECKPOINT_PATH:str = "checkpoints/"


KAFKA_BROKER_CONTAINER = "kafka:9093"
KAFKA_BROKER_HOST = "localhost:9092"

IS_CONTAINER = os.environ.get("RUNNING_IN_CONTAINER", "0") == "1"

BOOTSTRAP_SERVERS = KAFKA_BROKER_CONTAINER if IS_CONTAINER else KAFKA_BROKER_HOST
