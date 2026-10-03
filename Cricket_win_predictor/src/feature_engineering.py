
import pandas as pd
import numpy as np

def create_features(match_df, deliveries):

    delivery_df = match_df.merge(deliveries,on='match_id')
    delivery_df = delivery_df[delivery_df['inning']==2]

    delivery_df['current_score'] = delivery_df.groupby('match_id')['total_runs_y'].cumsum()

    delivery_df['runs_left'] = delivery_df['total_runs_x'] - delivery_df['current_score']

    delivery_df['balls_left'] = 126 - (delivery_df['over']*6 + delivery_df['ball'])

    delivery_df['player_dismissed'] = delivery_df['player_dismissed'].fillna("0")
    delivery_df['player_dismissed'] = delivery_df['player_dismissed'].apply(lambda x:0 if x=="0" else 1)

    wickets = delivery_df.groupby('match_id')['player_dismissed'].cumsum()

    delivery_df['wickets'] = 10 - wickets

    delivery_df['crr'] = (delivery_df['current_score']*6)/(120-delivery_df['balls_left'])

    delivery_df['rrr'] = (delivery_df['runs_left']*6)/delivery_df['balls_left']

    delivery_df['result'] = delivery_df.apply(
        lambda row: 1 if row['batting_team']==row['winner'] else 0, axis=1
    )

    final_df = delivery_df[['batting_team','bowling_team','city','runs_left',
                            'balls_left','wickets','total_runs_x','crr','rrr','result']]

    final_df.dropna(inplace=True)
    final_df = final_df[final_df['balls_left']!=0]

    return final_df