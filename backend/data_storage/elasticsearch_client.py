from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def store_to_elasticsearch(post, sentiment_score):
    doc = {
        'post': post,
        'sentiment': sentiment_score
    }
    es.index(index='reddit', body=doc)

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

def get_metrics(subreddit):
    response = es.search(
        index="reddit",
        body={
            "query": {"match": {"subreddit": subreddit}},
            "aggregations": {
                "upvotes": {"sum": {"field": "upvotes"}},
                "comments": {"sum": {"field": "comments"}}
            }
        }
    )
    return response['aggregations']
