from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'telemetry-data',
    bootstrap_servers='127.0.0.1:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print("Received:", message.value)