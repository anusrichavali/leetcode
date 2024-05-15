# Write your MySQL query statement below
select tweet_id from Tweets WHERE CHAR_LENGTH(content) > 140 OR
      LENGTH(content)- LENGTH(REPLACE(content, '@', '')) > 3 OR
      LENGTH(content)- LENGTH(REPLACE(content, '#', '')) > 3 order by tweet_id asc;
