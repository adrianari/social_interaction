import pandas as pd
import re


# Read data:
data = pd.read_csv("data/trump_twitter_2009-2020.csv", sep=",")


def get_retweeted_accounts(trump_twitter):
    """Returns a list of every twitter account DT ever retweeted"""
    
    # Filter rows with retweets only:
    retweets = trump_twitter[trump_twitter["isRetweet"] == "t"]
    
    # Drop all columns except "text" and reindex column:
    handles = retweets.drop(["id", "isRetweet", "isDeleted", "device", "favorites", "retweets", "date"], axis=1)
    handles = handles.reset_index()
    handles = handles.drop("index", axis=1)
    
    # Filter the account handles with regex:
    retweeted_accounts = []

    for index, row in handles.iterrows():
        account = re.search(r'(@)\w+', str(row)).group()
        retweeted_accounts.append(account)
    
    return retweeted_accounts


def get_number_of_retweets(tweets):
    """Returns a list of accounts, sorted by number of retweets."""
    
    # Empty dicts, later used for list concatenation:
    retweet_counter = {"account_name": [], "retweet_count": []}
    
    # Fill the lists in the dict with the respective values:
    for account in tweets:
        if account not in retweet_counter["account_name"]:
            retweet_counter["account_name"].append(account)
            retweet_counter["retweet_count"].append(1)
        else:
            account_position = retweet_counter["account_name"].index(account)
            retweet_counter["retweet_count"][account_position] += 1
    
    # Concatenate the lists in the retweet_counter dict, return single dictionary:
    retweets_pairing = {retweet_counter["account_name"][i]:
                        retweet_counter["retweet_count"][i]
                        for i in range(len(retweet_counter["account_name"]))}
    
    # Sort the key-value-pairs in the retweets_pairing dictionary in descending order: 
    retweets_sorted = sorted(retweets_pairing.items(), key = lambda kv: kv[1], reverse = True)
    
    # Return the sorted values:
    return retweets_sorted


# Applying the functions and getting the top 100 retweeted accounts:
all_retweets = get_number_of_retweets(get_retweeted_accounts(data))
top100 = all_retweets[:100]
top100
