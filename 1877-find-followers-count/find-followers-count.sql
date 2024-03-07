# Write your MySQL query statement below
Select user_id, COUNT(follower_id) as followers_count FROM Followers Group By user_id Order by user_id ASC;