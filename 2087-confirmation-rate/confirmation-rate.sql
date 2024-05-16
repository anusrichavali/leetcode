# Write your MySQL query statement below
select u.user_id, IFNULL(round(sum(c.action="confirmed")/count(*), 2), 0) as confirmation_rate from signups u left join confirmations c on u.user_id = c.user_id group by user_id;