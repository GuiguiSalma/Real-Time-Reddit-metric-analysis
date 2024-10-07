from data_ingestion.kafka_producer import reddit_producer
from data_processing.spark_processing import process_reddit_stream
from flask import Flask, jsonify
from data_storage.elasticsearch_client import get_country_metrics

app = Flask(__name__)

def main():
    print("Starting Reddit Metric Analysis...")

    # Start Kafka producer to stream Reddit posts
    reddit_producer()

    # Start Spark Streaming to process data in real-time
    process_reddit_stream()

# Flask route to serve country metrics for the frontend
@app.route('/api/country/<country_name>', methods=['GET'])
def get_metrics_for_country(country_name):
    try:
        # Get metrics from Elasticsearch for the selected country
        metrics = get_country_metrics(country_name)
        return jsonify(metrics), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    main()
    # Run the Flask app to serve the API
    app.run(host="0.0.0.0", port=5000)
