
import pandas as pd

def load_data():
    matches = pd.read_csv("data/matches.csv")
    deliveries = pd.read_csv("data/deliveries.csv")
    return matches, deliveries


def merge_data(matches, deliveries):

    total_score = deliveries.groupby(['match_id','inning']).sum()['total_runs'].reset_index()
    total_score = total_score[total_score['inning'] == 1]

    match_df = matches.merge(total_score[['match_id','total_runs']],
                             left_on='id',
                             right_on='match_id')

    return match_df