import time
import pandas as pd

from kafka import KafkaProducer

from common.config import (
  ONLINE_DATA_PATH, 
  TARGET_COL, 
  PRODUCER_TOPIC,
  BOOTSTRAP_SERVERS
)


producer = KafkaProducer(
  bootstrap_servers=BOOTSTRAP_SERVERS, 
  security_protocol="PLAINTEXT",
  value_serializer=lambda v: v.encode("utf-8")
)

df = pd.read_csv(ONLINE_DATA_PATH)

df = df.drop(columns=[TARGET_COL])

json_lines = df.to_json(orient="records", lines=True)

for line in json_lines.splitlines():
  producer.send(PRODUCER_TOPIC, value=line)
  print(f"Produced: {line}")
  time.sleep(1)

producer.flush()
producer.close()
