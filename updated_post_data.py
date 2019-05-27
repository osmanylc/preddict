#!/home/osmany/anaconda3/envs/reddit/bin/python

import sys
import csv

import pandas as pd
import numpy as np
import praw


def current_post_data(start_from=0):
    filename = 'post_data_from_{}.csv'.format(start_from)
    df = pd.read_csv('aug2018.csv')
    reddit = praw.Reddit('preddit')
    cols = ['index', 'score', 'ups', 'downs', 'num_comments', 'gilded', 'op_created']
    
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, cols)
        writer.writeheader()

        for i in range(start_from, df.shape[0]):
            df_row = df.loc[i]
            data_row = [i]

            post = reddit.submission(url=df_row.url)
            if post is not None:
                author = post.author
                data_row.extend([post.score, post.ups, post.downs, post.num_comments, post.gilded])
                
                if author is not None:
                    data_row.append(author.created_utc)
                else:
                    data_row.append('nan')
            else:
                data_row.extend(len(cols)*['nan'])
            
            writer.writerow(dict(zip(cols,data_row)))
            if i+1 % 100 == 0:
                print(i)
            
            
            
if __name__ == '__main__':
    if len(sys.argv) > 1:
        current_post_data(int(sys.argv[1]))
    else:
        current_post_data()

