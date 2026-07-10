from kafka import KafkaConsumer
import json
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="ott_db",
    user="postgres",
    password="Naincy"
)

cursor = conn.cursor()

# Connect to Kafka
consumer = KafkaConsumer(
    "video-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Waiting for events...")

for message in consumer:
    try:
        event = message.value
        video_id = event["video_id"]

        cursor.execute(
            """
            INSERT INTO video_views (video_id, total_views)
            VALUES (%s, 1)
            ON CONFLICT (video_id)
            DO UPDATE SET total_views = video_views.total_views + 1;
            """,
            (video_id,)
        )

        conn.commit()
        print(f"Updated views for video {video_id}")

    except Exception as e:
        print(f"Error processing event: {e}")