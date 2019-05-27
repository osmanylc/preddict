#!/home/osmany/anaconda3/envs/reddit/bin/python

import sys
import csv
import time

import pandas as pd
import numpy as np
import praw


def current_post_data(start_from=0):
    filename = 'post_data_from_{}.csv'.format(start_from)
    df = pd.read_csv('aug2018.csv')
    reddit = praw.Reddit('preddit')
    cols = ['index', 'score', 'ups', 'downs', 'num_comments', 'gilded']
    s_t = time.time()
    
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, cols)
        writer.writeheader()

        for i in range(start_from, df.shape[0]):
            df_row = df.loc[i]
            data_row = [i]

            post_vals = _get_post_values(reddit, df_row.url, cols[1:])
            data_row.extend(post_vals)
            
            writer.writerow(dict(zip(cols,data_row)))
            if (i-start_from + 1) % 100 == 0:
                print('Processed posts: {}'.format(i-start_from + 1))
                print('Time elapsed: {:.2f}s'.format(time.time() - s_t))
                print('=======================')
                
                
def _get_post_values(reddit, url, attrs):
    post = reddit.submission(url=url)
    post_vals = []
    
    if post is None:
        return len(attrs) * ['nan']
        
    _ = len(post.title)
    post_vars = vars(post)
    
    for a in attrs:
        if a in post_vars:
            post_vals.append(post_vars[a])
        else:
            post_vals.append('nan')
    
    return post_vals
            
            
            
if __name__ == '__main__':
    if len(sys.argv) > 1:
        current_post_data(int(sys.argv[1]))
    else:
        current_post_data()

