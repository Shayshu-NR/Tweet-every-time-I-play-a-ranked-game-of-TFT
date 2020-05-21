#Send a tweet out describing how the TFT game went
#~~~~~Libraries~~~~~
import json
import tweepy as tw
import pandas as pd
from twitter_keys import *
#~~~~~~~~~~~~~~~~~~~~
 
class Twitter_Bot():
    def authorize(self, consumer, comsumer_secret):
        auth = tw.OAuthHandler(consumer, consumer_secret)

        return auth
    
    def access_toke(self, auth, token, token_secret):
        auth.set_access_token(token, token_secret)

        return auth
    
    def get_api(self, auth):
        api = tw.API(auth, wait_on_rate_limit = True)

        return api
    
    def update_status(self, api, status):
        api.update_status(status)

        return