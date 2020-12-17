## HSLU Group Project - Analysis of Social Interactions

The goal of this project was creating and analyzing a network of twitter accounts based
on the tweets by U.S. president Donald Trump. We identified the top 100 accounts Trump
retweeted most often since the beginning of his tenure on January 20, 2016. A network of 
these accounts was created and analyzed in various ways.

The structure of this project is as follows:

1. *get_retweets* contains a script to identify the top 100 accounts retweeted by Donald Trump
which form the basis for the network.
2. *get_friends* contains a script which was used to obtain Twitter data for those 100 accounts
via the Twitter API.
3. *friends* contains the raw data.
4. *data_cleaning* contains a script for cleaning and harmonizing the raw data in a way
that can be used for building the network and analysis.
5. *Gephi* contains analysis done with the *Gephi* software.
6. *Clustering* contains a script for clustering the accounts in various ways.
7. *rich_club_analysis* contains an analysis of the network based on the rich club
algorithm.
