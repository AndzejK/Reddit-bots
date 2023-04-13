import praw 
import os
from datetime import datetime,timedelta
# Instance
reddit = praw.Reddit(
    # read-only
    client_id=os.getenv("clientIDreddit"),
    client_secret=os.getenv("clientSecretReddit"),
    user_agent="Andrey",
    # write and read
    password=os.getenv("passwordReddit"),
    username="krupoves",
)

# where we're going to post - subreddit
subreddit = reddit.subreddit("pythonsandlot") #r/pythonsandlot
title="Memento Mori"
content="""
Whatever you do, do it 100%. 
When you work, work. 
When you laugh, laugh. 
When you eat, eat like it's your last meal.
    G. -> Tony Lip
"""
# Submission 
subreddit.submit(title=title,selftext=content)