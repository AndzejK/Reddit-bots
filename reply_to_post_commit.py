import praw 
import os
from datetime import datetime,timedelta
# Instance
reddit = praw.Reddit(
    # read-only
    client_id=os.getenv("clientIDreddit"), # clientIDreddit
    client_secret=os.getenv("clientSecretReddit"), #clientSecretReddit
    user_agent="Andrey",
    # write and read
    password=os.getenv("passwordReddit"), #passwordReddit
    username="krupoves",
)
# Getting info abount community dedicated to a specific topic or theme - SUBREDDIT
subreddit = reddit.subreddit("sydney") #r/sydney

for topic in subreddit.new():
    current_time=datetime.utcnow() 
    topic_time=datetime.utcfromtimestamp(topic.created) # coverted from sec to 2023-04-13 01:35:59 format
        # print(current_time,topic_time) #2023-04-13 06:44:54.634701 1681171570.0
    delta_time=current_time-topic_time
        # print(delta_time)
    if delta_time<=timedelta(hours=48):
        if "aggressive" in topic.title.lower():
            print(topic.title)
            topic.reply("Hey, people just being people.")
        