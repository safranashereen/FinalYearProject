try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN = '2344935827-E706CCyvwEx3Gzvolv19wOyYs1HpOPEJzdrwg5o'
ACCESS_SECRET = 'vrXDFs6aHcQdeFH7HnsMztnoPoLvSMdEXdK75o49THvsY'
CONSUMER_KEY = 'YiJqzFRh4FvMmNxrZ1qqZAG6r'
CONSUMER_SECRET = 'u2V4Xd9MV3Uf5e7iSrqf03FyiQAkKdfMFDNn5Y4Ii45kp1Vkdp'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.filter(track="Kill", language="en")
twitter_userstream = TwitterStream(auth=oauth, domain='userstream.twitter.com')

tweet_count =100
for tweet in iterator:
    tweet_count -= 1
    print json.dumps(tweet)  
         
    if tweet_count <= 0:
        break
