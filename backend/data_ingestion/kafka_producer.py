import json
from kafka import KafkaProducer
from praw_config import get_reddit_client

def get_country_from_subreddit(subreddit_name):
    country_mapping = {
        'morocco': 'Morocco',
        'france': 'France',
        'usa': 'USA',
        'unitedkingdom': 'United Kingdom',
        'canada': 'Canada',
        'australia': 'Australia',
        'india': 'India',
        'germany': 'Germany',
        'japan': 'Japan',
        'brazil': 'Brazil',
        'southafrica': 'South Africa',
        'china': 'China',
    }
    return country_mapping.get(subreddit_name.lower(), 'Unknown')

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
            'country': get_country_from_subreddit(submission.subreddit.display_name),  
        }
        producer.send('reddit-topic', post)
        print(f"Produced message to Kafka: {post['title']}, Country: {post['country']}")
