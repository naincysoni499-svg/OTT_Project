from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_event(event):
    try:
        producer.send("video-events", event)
        producer.flush()
        print("Event sent successfully!")
    except Exception as e:
        print(f"Error sending event: {e}")