from elasticsearch import Elasticsearch


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Store a document to Elasticsearch with the given sentiment score
def store_to_elasticsearch(post, sentiment_score):
    doc = {
        'post': post,
        'sentiment': sentiment_score
    }
    es.index(index='reddit', body=doc)

# Get the top words from a given subreddit (optional,add the ones you want)
def get_top_words(subreddit):
    response = es.search(
        index="reddit",
        body={
            "query": {"match": {"subreddit": subreddit}},
            "aggregations": {
                "top_words": {"terms": {"field": "post.keyword", "size": 10}}
            }
        }
    )
    return response['aggregations']['top_words']['buckets']

# Get metrics for a specific country from Elasticsearch
def get_country_metrics(country):
    response = es.search(
        index="reddit-country-metrics", 
        body={
            "query": {"match": {"country": country}},  
            "aggs": {
                "total_upvotes": {"sum": {"field": "total_upvotes"}},
                "total_comments": {"sum": {"field": "total_comments"}},
                "avg_sentiment": {"avg": {"field": "avg_sentiment"}}
            }
        }
    )

    # Extract aggregated results
    metrics = response['aggregations']
    return {
        'total_upvotes': metrics['total_upvotes']['value'],
        'total_comments': metrics['total_comments']['value'],
        'avg_sentiment': metrics['avg_sentiment']['value']
    }
