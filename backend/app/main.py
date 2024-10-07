from data_ingestion.kafka_producer import reddit_producer
from data_processing.spark_processing import process_reddit_stream

def main():
    print("Starting Reddit Metric Analysis...")

    # Start Kafka producer to stream Reddit posts
    reddit_producer()

    # Start Spark Streaming to process data in real-time
    process_reddit_stream()

if __name__ == "__main__":
    main()
