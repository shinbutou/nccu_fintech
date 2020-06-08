# trump_tweets.py

# General
import tweepy
import pandas as pd
import numpy as np

# For plotting and visualization
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

'''
#We import out access keys:
from credentials import *

# API's setup
def twitter_setup():
	"""
	Utility function to setup the Twitter's API
	with our access keys provided.
	"""
	# Authentication and access using keys:
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

	# Return API with authentication:
	api = tweepy.API(auth)
	return api

# create an extractor object:
extractor = twitter_setup()
RawData=''
# create a tweet list as follows:
tweets = extractor.user_timeline(screen_name='realDonaldTrump', count=200)
print('Number of tweets extracted: {}.\n'.format(len(tweets)))

# print the mist recent 5 tweets:
print('5 recent tweets:\n')
for tweet in tweets[:5]:
	print(tweet.text)
	print()


### Creating a pandas DataFrame ###

# create a pandas dataframe as follows:
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# display the first 10 elements of the dataframe:
display(data.head(10))

# internal methods of a single tweet object:
print(dir(tweets[0]))

# info from the first tweet:
fir = tweet[0]
print(fir.id)
print(fir.created_at)
print(fir.source)
print(fir.favorite_count)
print(fir.retweet_count)
print(fir.geo)
print(fir.coordinates)
print(fir.entities)

# add relevant info to our dataframe
data['len'] 	= np.array([len(tw.text) for tw in tweets])
data['id']		= np.array([tw.id for tw in tweets])
data['date']	= np.array([tw.date for tw in tweets])
data['source']		= np.array([tw.source for tw in tweets])
data['likes']		= np.array([tw.favorite_count for tw in tweets])
data['rts']		= np.array([tw.tetweet_count for tw in tweets])


### Visualization and basic statistics ###

# extract the mean of lengths:
mean = np.mean(data['len'])
print('The length\'s average in tweets: {}'.format(mean))

# extract the tweet with more FAVs and more RTs
fav_max = float('-inf')
fav = None
rt_max = float('-inf')
rt = None
for a, likes in enumerate(data['likes']):
	if fav_max<likes:
		fav_max = likes
		fav = a

for a, rts in enumerate(data['rts']):
	if rt_max<rts:
		rt_max = rts
		rt = a
	# fav_max = np.max(data['likes'])
	# rt_max = np.max(data['rts'])

	# fav = data[data.likes==fav_max].index[0]
	# rt 	= data[data.rts==rt_max].index[0] 

# Max FAVs:
print("The tweet with more likes is: \n{}".format(data['tweets'][fav]))
print("Number of likes: {}".format(fav_max))
print("{} characters.\n".format(data['len'][fav]))

# Max RTs:
print("The tweet with more retweets is: \n{}".format(data['tweets'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))

# We create time series for data:

tlen = pd.Series(data=data['len'].values, index=data['Date'])
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])
 
# Lenghts along time:
tlen.plot(figsize=(16,4), color='r');

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True);


# We obtain all possible sources:
sources = []
for source in data['Source']:
	if source not in sources:
		sources.append(source)

# We print sources list:
print("Creation of content sources:")
for source in sources:
	print("* {}".format(source))

# We create a numpy vector mapped to labels:
percent = np.zeros(len(sources))

for source in data['Source']:
	for index in range(len(sources)):
		if source == sources[index]:
			percent[index] += 1
			pass

percent /= 100

# Pie chart:
pie_chart = pd.Series(percent, index=sources, name='Sources')
pie_chart.plot.pie(fontsize=11, autopct='%.2f', figsize=(6, 6));

'''
import w2l

list = w2l.word2list('top100.txt')
print(list)







