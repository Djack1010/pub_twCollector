import sys
import os
import tweepy
import settings
from StreamListener import StreamListener
from datetime import datetime
import utility

# set up the authentication object using Twitter credentials and OAuthHandler method
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

# pass the auth object to the API to authenticate, obtaining an object referencing the Twitter API
api = tweepy.API(auth)

# check that the authentication was successful with the me() method and print your own Twitter name
myself = api.me()
assert myself
print("Account di " + myself.name)


while True:
    now = datetime.now()
    # NB the variable 'today' needs same format in StramListener 'today', changes needs to be propagated!
    today = "{:02d}{:02d}/{:02d}{:02d}{:02d}".format(now.month, now.year, now.day, now.month, now.year)

    if not os.path.isdir("db/{:02d}{:02d}".format(now.month, now.year)):
        os.mkdir("db/{:02d}{:02d}".format(now.month, now.year))
    if not os.path.isdir("logs/{:02d}{:02d}".format(now.month, now.year)):
        os.mkdir("logs/{:02d}{:02d}".format(now.month, now.year))

    utility.print_on_file("Starting Loop StreamListener", today)

    stream_listener = StreamListener(date=str(today))
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=settings.TRACK_TERMS)
