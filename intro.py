import praw 
import os
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
# The post's link
url="https://www.reddit.com/r/sydney/comments/12g04er/where_will_the_new_gentrified_part_of_sydney_be/" 

post=reddit.submission(url=url)
# Getting the title of the post
print(post.title)
# Getting the content of the post
print(post.selftext)

# Getting the TOP lvl comments of the post, without answers int he comments
for index,comment in enumerate(post.comments):
    print(f"No.{index}\n,{comment.body}\n")