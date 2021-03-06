import pandas as pd
from EskomFunctions.function4 import extract_municipality_hashtags
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)

assert extract_municipality_hashtags(twitter_df).iloc[5,2] == 'Johannesburg'
assert extract_municipality_hashtags(twitter_df).iloc[4,3] == ['#eskomfreestate', '#mediastatement']

