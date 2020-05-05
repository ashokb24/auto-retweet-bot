# AUTOMATED-RETWEET-BOT

# Description : 
 This bot has been created to simply and reduce the work in retweet a tweet from a existing twitter user.
 
# Solution Overview
The project is hosted on AWS Cloud infra in the form of serverless components. Automated tweet bot is a stateless software bot which meant to handle the below functionalities on behalf of the twitter user thereby reducing the work of twitter user spending time in opening the twitter app from his mobile app/ desktop application. There is a need to build a autoamted tweet bot so that it can be scheduled to invoke the twitter api on a daily basis at a specified time and greet the tweet user. 

# Use-Case Constraints
- Solution to be build in AWS Cloud
- Solution to be serverless
- Solution can use any open source library wherever applicable.

# RETWEEET Serverless Service
Auto Service runs for every day at morning 4 AM at UTC timezone ( IST 8.30 AM) 30 mins and retrieves the given user timeline from 
his twitter account using twython API Python library. Bot accepts the below parameters to operate
- retweet_from_user_id : Twitter User Id from which you have to re-tweet a tweet
- tweet_hashtag : Hastag associated with the tweet which you want to re-tweet
- time_line_count : User Time line count to retrieve to user time line of the given user. 
    ( eg : If you pass 5, it will be retrieve the top 5 user time line from a given user)
