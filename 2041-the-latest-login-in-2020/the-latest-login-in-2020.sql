# Write your MySQL query statement below
Select user_id, MAX(time_stamp) as last_stamp From Logins where year(time_stamp) = 2020 Group By user_id;