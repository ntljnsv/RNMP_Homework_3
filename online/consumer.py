import json

from kafka import KafkaConsumer

from common.config import CONSUMER_TOPIC, BOOTSTRAP_SERVERS


consumer = KafkaConsumer(
  CONSUMER_TOPIC,
  bootstrap_servers=BOOTSTRAP_SERVERS,
  auto_offset_reset='earliest',
  enable_auto_commit=False,
  value_deserializer=lambda message: json.loads(message.decode('utf-8'))
)

try:
  for message in consumer:
    print(f"Received message: {json.dumps(message.value, indent=4)}")

except KeyboardInterrupt:
  pass

finally:
  consumer.close()