import praw
from kafka import KafkaProducer
import json
from praw_config import get_reddit_client

def reddit_producer():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    reddit = get_reddit_client()
    for submission in reddit.subreddit('all').stream.submissions():
        post = {
            'title': submission.title,
            'selftext': submission.selftext,
            'subreddit': submission.subreddit.display_name,
            'created_utc': submission.created_utc,
            'upvotes': submission.ups,
            'comments': submission.num_comments,
        }
        producer.send('reddit-topic', post)
        print(f"Produced message to Kafka: {post['title']}")

if __name__ == "__main__":
    reddit_producer()
