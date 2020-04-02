import tweepy
import time

auth = tweepy.OAuthHandler(
    'aaaaaaaaaa', 'bbbbbbbb')
auth.set_access_token('cccccccccccc',
                      'ddddddddddddd')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Ajeasmith':
#         follower.follow()
#         break
