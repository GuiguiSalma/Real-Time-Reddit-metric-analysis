import praw

def get_reddit_client():
    reddit = praw.Reddit(
        client_id='REMOVED',
        client_secret='U AIN'T GETTING MY KEY',
        user_agent='Metric Analysis'
    )
    return reddit
