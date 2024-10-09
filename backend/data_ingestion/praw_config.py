import praw

def get_reddit_client():
    reddit = praw.Reddit(
        client_id='no',
        client_secret='non',
        user_agent='LA27'
    )
    return reddit
