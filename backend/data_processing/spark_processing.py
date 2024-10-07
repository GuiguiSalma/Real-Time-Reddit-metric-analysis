from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, from_json, sum, avg
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from textblob import TextBlob

# UDF to analyze sentiment using TextBlob
def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

def process_reddit_stream():
    spark = SparkSession.builder.appName("Reddit Sentiment Analysis").getOrCreate()

    # Define the schema for the Reddit data coming from Kafka
    reddit_schema = StructType([
        StructField("title", StringType()),
        StructField("selftext", StringType()),
        StructField("subreddit", StringType()),
        StructField("upvotes", IntegerType()),
        StructField("comments", IntegerType()),
        StructField("country", StringType()),  # Assuming country data exists
        StructField("created_utc", StringType())
    ])

    # Register the UDF for sentiment analysis
    sentiment_udf = udf(analyze_sentiment)

    # Read the data stream from Kafka
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "reddit-topic") \
        .load()

    # Extract the value as a string and parse it using the schema
    df = df.selectExpr("CAST(value AS STRING) as value")
    df = df.withColumn("value", from_json(col("value"), reddit_schema))

    # Add sentiment column
    df = df.withColumn("sentiment", sentiment_udf(col("value.selftext")))

    # Aggregate data by country
    country_agg = df.groupBy("value.country") \
        .agg(
            sum("value.upvotes").alias("total_upvotes"),
            sum("value.comments").alias("total_comments"),
            avg("sentiment").alias("avg_sentiment")
        )

    # Write results to Elasticsearch
    country_agg.writeStream \
        .format("org.elasticsearch.spark.sql") \
        .option("checkpointLocation", "/path/to/checkpoint") \
        .option("es.nodes", "localhost:9200") \
        .start("reddit-country-metrics")  # Index in Elasticsearch

    spark.streams.awaitAnyTermination()
