# twitter APIs
import twitter
from twitter_api_keys import *

def twitter_stream(request):
    api = twitter.Api(consumer_key=twitter_consumer_key,
                      consumer_secret=twitter_consumer_secret,
                      access_token_key=twitter_access_token_key,
                      access_token_secret=twitter_access_token_secret)
    statuses = api.GetUserTimeline('djangoproject')             
    return {'statuses': statuses}