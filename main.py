import pandas as pd
import tweepy as tw
from pytz import timezone
import pytz
import warnings

tz=pytz.timezone('Asia/Bangkok')
warnings.filterwarnings("ignore")

class tweet_func:

    def __init__(self, api_key, api_secret, access_token, access_secret, search_words, count):

        self.auth = tw.OAuthHandler(api_key, api_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = tw.API(self.auth, wait_on_rate_limit=True)

        self.search_words = search_words
        self.count = count
        self.tweet_text = None
        self.users_locs = None

    def run(self):
        self.tweets = tw.Cursor(self.api.search,
                    q=self.search_words,
                    lang="th", #language
                    result_type="recent").items(self.count)

        self.users_locs = []
        for tweet in self.tweets:
            try:
                self.users_locs.append([tweet.user.screen_name,tweet.text.split(":")[0].split("@")[1],tweet.text , tweet.user.location,tz.localize(tweet.created_at),tweet.retweet_count,tweet.user.profile_image_url_https])
            except:
                pass

            self.tweet_text = pd.DataFrame(data=self.users_locs,  # create cell
                            columns=['user','RT','text' ,"location",'date','count','url'])


# %%
if __name__ == "__main__":

    ######################## tweet api ########################
    api_key = ' '
    api_secret = ' '
    access_token = ' '
    access_secret = ' '
    ###########################################################

    search_words = ' '
    count = None

    ###########################################################
    
    tweets = tweet_func(api_key, api_secret, access_token, access_secret, search_words, count)
    tweets.run()


# %%
    tweets.tweet_text
