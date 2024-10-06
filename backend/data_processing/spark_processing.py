from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from textblob import TextBlob
from kafka import KafkaConsumer
import json

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Reddit Sentiment Analysis") \
    .getOrCreate()

# UDF for sentiment analysis
def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

sentiment_udf = udf(analyze_sentiment)

# Kafka consumer
def process_reddit_stream():
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "reddit-topic") \
        .load()
    
    # Process the Kafka stream
    df = df.selectExpr("CAST(value AS STRING)")
    df = df.withColumn("sentiment", sentiment_udf(df.value))

    # Write results to Elasticsearch
    df.writeStream \
      .format("org.elasticsearch.spark.sql") \
      .option("checkpointLocation", "/path/to/checkpoint") \
      .option("es.nodes", "localhost:9200") \
      .start("reddit-sentiment")

if __name__ == "__main__":
    process_reddit_stream()
