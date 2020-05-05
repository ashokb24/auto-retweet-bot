from twython import Twython

app_key = 'EeGLxQ6lo4MzZ4k7pZQIRxmJa'
app_secret = 'csO2AgepbdMi8MKTxr7kGqRIdaBvzSXJcxPuClpXIMaT4GqeVy'
oauth_token = '840889837-QK0gIxZnzLSLBaHhSTpz2GbAAzCsXDtV6rDoZ3Xr'
oauth_token_secret = 'hZq8AtKlfhOtQM3Cu1hQ7TFvzLuJPNbBnhNm9YhtXsl2Z'
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
interested_hashtag = "#SadhguruQuotes"
retweet_from_user_id = "SadhguruJV"

if len(interested_hashtag) != 0:
    user_timelines = twitter.get_user_timeline(screen_name=retweet_from_user_id, count=5, trim_user="t",
                                               exclude_replies="true", include_rts="false", tweet_mode="extended")
    for user_time_line in user_timelines:
        if interested_hashtag in user_time_line['full_text']:
            twitter.retweet(status="RETWEET FROM MY PERSONAL BOT ASSISTANT",id=user_time_line['id'])

else:
    user_timelines = twitter.get_user_timeline(screen_name=retweet_from_user_id, count=5, trim_user="t",
                                               exclude_replies="true", include_rts="false")
    for user_time_line in user_timelines:
        if interested_hashtag in user_time_line['text']:
            twitter.retweet(status="RETWEET FROM MY PERSONAL BOT ASSISTANT",id=user_time_line['id'])
