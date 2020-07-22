import tweepy
import time
auth=tweepy.OAuthHandler('puaZEUdP4C0tWhDNomzqwnINe','RQ3FnvrOcFqWLDeF6Bn9841k3qjV3KZifJRfVftcSMAWXAIpZC')
auth.set_access_token('1285971719383990274-4SJot5O94cw7eoby1PHGribcxpSqg7','FSQEdjiELoK0Ct5riHWjkbB3EX3qFHf8UZCkiAOwyVbnQ')
api= tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user=api.me()
search=("microsoft")
nrTweets=500
for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('Tweet liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break        
