from twython import Twython
import json
import os
import boto3


def re_tweet_a_user_status(event, context):
    event_string = json.dumps(event)
    data = json.loads(event_string)
    # Reading the inputs from the event
    retweet_from_user_id = data['retweet_from_user_id']
    interested_hashtag = data['tweet_hashtag']
    time_line_count = data['time_line_count']

    # calling the method to read the twitter secret from S3
    secret_bag = read_twitter_secrets_from_s3(bucket_name=os.environ['AUTO_RETWEET_BUCKET'],
                                              file_name=os.environ['FILE_NAME'],
                                              region_name=os.environ['S3_REGION'])
    app_key = secret_bag['consumer_key']
    app_secret = secret_bag['consumer_secret']
    oauth_token = secret_bag['oauth_token']
    oauth_token_secret = secret_bag['oauth_token_secret']

    twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

    if len(interested_hashtag) != 0:
        user_timelines = twitter.get_user_timeline(screen_name=retweet_from_user_id, count=time_line_count,
                                                   trim_user="t",
                                                   exclude_replies="true", include_rts="false", tweet_mode="extended")
        for user_time_line in user_timelines:
            if interested_hashtag in user_time_line['full_text']:
                print(user_time_line['full_text'])
                twitter.retweet(status="RETWEET FROM MY PERSONAL BOT ASSISTANT", id=user_time_line['id'])
                twitter.create_favorite(id=user_time_line['id'])

    return "BOT FINISHED RE-TWEET SUCCESSFULLY"


def read_twitter_secrets_from_s3(bucket_name=None, file_name=None, region_name=None):
    s3client = boto3.client('s3', region_name=region_name)
    # Create a file object using the bucket and object key.
    fileobj = s3client.get_object(Bucket=bucket_name, Key=file_name)
    # open the file object and read it into the variable filedata.
    filedata = fileobj['Body'].read()
    # file data will be a binary stream.  We have to decode it
    contents = filedata.decode('utf-8')
    # return the json object
    return json.loads(contents)
