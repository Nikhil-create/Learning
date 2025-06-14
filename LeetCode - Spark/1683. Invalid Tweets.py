# 1683. Invalid Tweets

data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

tweets_df = spark.createDataFrame(tweets)

tweets_df = tweets_df\
    .filter((length(tweets_df.content) > 15))\
        .select(tweets_df.tweet_id)

tweets_df.display()