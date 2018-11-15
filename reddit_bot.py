import praw
from reddit_auth import *

reddit = praw.Reddit(user_agent,
                     client_id,
                     secret,
                     )

sub = reddit.subreddit('python')

print(sub)
