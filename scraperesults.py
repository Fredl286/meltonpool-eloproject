import pandas as pd
import numpy as np

# Options for Libraries
pd.options.mode.chained_assignment = None  # default='warn'

# Division and season
division = [1,2,3,4,5]
season = [14,13,12,11,10,9,8,7,6,5,4,3,2,1]

for y in season:
    for x in division:
        url_dates = "https://www.meltonpool.uk/division.php?division=" + str(x) + "&season=" + str(y)
        dfs = pd.read_html(url_dates)
        e = (len(dfs))-1
        
        for x in range (2,e):
            try:
                df =(dfs[x])
                df = df[['FRAMES.1','FRAMES.2', 'FRAMES.4', 'FRAMES.5']]
                df.rename(columns={'FRAMES.1': 'Team 1', 'FRAMES.2': 'Score 1', "FRAMES.4": "Score 2", "FRAMES.5": "Team 2"}, inplace=True)
                df.drop(labels=[9,10,], axis = 0, inplace=True)
                df.replace(np.nan, 0, inplace=True)
                print(df)
                df.to_csv('poolresults.csv', mode='a', header=False)
            except KeyError:
                pass


