import tweepy
import pandas as pd
import time


# Set up Twitter API credentials:
API_Key = "---HIER API KEY EINGEBEN---"
API_Secret = "---HIER API SECRET KEY EINGEBEN---"

# Authorization of key and secret:
auth = tweepy.AppAuthHandler(API_Key, API_Secret)

# Calling the API:
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


# Define function to fetch friends list:
def get_friends(user_id):
    """
    :param user_id: Twitter screen name of an account
    This function writes a CSV file with all friends of a
    specific Twitter user.
    """
    # Empty lists which are filled with the friends screen names:
    friends_cursor = []
    friends_list = []
    
    # Using a cursor to fetch all friends of an account
    # and write the result in list friends_cursor:
    page_count = 0
    for i, friend in enumerate(tweepy.Cursor(api.friends, id = user_id, count = 200).pages()):
        print(f"Getting page {i} for friends")
        friends_cursor += friend
    
    # Extract the screen names from the friends_cursor results
    # and write only the screen names to list friends_list:
    for friend in friends_cursor:
        friends_list.append(friend.screen_name)
    
    # Transform the friends_list into a pandas DataFrame:
    friends_df = pd.DataFrame(friends_list)
    
    # Define path and filename to save CSV:
    filename = f"{user_id}_friends.csv"
    filepath = f"friends/{filename}"
    
    # Write CSV:
    friends_df.to_csv(filepath, index = False)


# Setup for using the function
## Der Variable "screen_name" EINEN Twitter Screen Name (Handle) zuweisen.
## Der entsprechende Account wird gesucht und der Handle wird danach für die
## Benennung der CSV-Datei verwendet.

screen_name = "---HIER SCREEN NAME EINGEBEN---"


# Fire up the function:

# Determine start time:
start_time = time.time()
print("Start time: " + str(start_time))

friends = get_friends(screen_name)

# Detrmine end time and time needed for execution:
print("Finishing time: " + str(time.time()))
print("Time for execution (sec.): " + str(time.time() - start_time))
