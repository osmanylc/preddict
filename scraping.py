import csv
import praw
import pandas as pd


def get_new_posts(sub, n):
    reddit = praw.Reddit('preddit')
    askreddit = reddit.subreddit(sub)
    new_posts = askreddit.new(limit=n)
    
    return new_posts
    

def save_post_data(posts, filename):
    features = ['id', 'post_time', 'title', 'op', 'op_created', 
            'link_karma', 'comment_karma']
    
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, features, dialect='unix')
        writer.writeheader()

        for post in posts:
            author = post.author
            data_row = [post.id, post.created, post.title,
                        author.name, author.created, 
                        author.link_karma, author.comment_karma]
            
            writer.writerow(dict(zip(features, data_row)))
            
            
def new_post_data(n):
    new_posts = get_new_posts('askreddit', n)
    save_post_data(new_posts, '{}_new_posts.csv'.format(n))
    
    
def read_post_data(filename):
    df = pd.read_csv(filename)
    
    df.post_time = pd.to_datetime(df.post_time, unit='s')
    df.op_created = pd.to_datetime(df.op_created, unit='s')
    
    return df

