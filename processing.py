import pandas as pd


def merge_post_info():
    creation_df = pd.read_csv('aug2018.csv')
    perf_df = pd.read_csv('post_data_from_0.csv')
    
    creation_df.drop(columns=['score', 'num_comments', 'gilded'], inplace=True)
    return pd.concat([creation_df, perf_df], axis=1)

