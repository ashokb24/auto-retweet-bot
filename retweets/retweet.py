from twython import Twython
import json
import os


def re_tweet_a_user_status(event, context):
    event_string = json.dumps(event)
    data = json.loads(event_string)
    retweet_from_user_id = data['retweet_from_user_id']
    interested_hashtag = data['interested_hashtag']
    time_line_count = data['time_line_count']
    print("retweet user id " +retweet_from_user_id)
    print("hashtag passed "+interested_hashtag)

    app_key = os.environ['CONSUMER_KEY']
    app_secret = os.environ['CONSUMER_SECRET']
    oauth_token = os.environ['OAUTH_TOKEN']
    oauth_token_secret = os.environ['OAUTH_TOKEN_SECRET']

    twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

    if len(interested_hashtag) != 0:
        user_timelines = twitter.get_user_timeline(screen_name=retweet_from_user_id, count=time_line_count, trim_user="t",
                                                  exclude_replies="true", include_rts="false", tweet_mode="extended")
        for user_time_line in user_timelines:
            if interested_hashtag in user_time_line['full_text']:
                twitter.retweet(status="RETWEET FROM MY PERSONAL BOT ASSISTANT", id=user_time_line['id'])

    return "BOT FINISHED RE-TWEET SUCCESSFULLY"
