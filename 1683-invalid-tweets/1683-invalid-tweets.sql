# Write your MySQL query statement below
SELECT tweet_id       
FROM Tweets
WHERE Length(Tweets.content) > 15