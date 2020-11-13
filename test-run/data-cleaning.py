import pandas as pd
import re

# Datenaufbereitung: Reduzieren der Daten auf die Twitter-Handles

# 1. Daten einlesen
sample_data = pd.read_csv("data/twitter-test-data.csv", sep=";")

# 2. Filtern der Zeilen mit Retweets (is_retweet == True)
retweets = sample_data[sample_data["is_retweet"] == True]

# 3. Drop aller Spalten ausser dem Tweet-Text und Reindex:
handles = retweets.drop(["source", "created_at", "retweet_count", "favorite_count", "is_retweet", "id_str"], axis=1)
handles = handles.reset_index()
handles = handles.drop("index", axis=1)

# 4. Herausfiltern der Handles
accounts = []

for index, row in handles.iterrows():
    # print(re.search(r'(@)\w+', str(row)).group())
    account = re.search(r'(@)\w+', str(row)).group()
    accounts.append(account)

accounts