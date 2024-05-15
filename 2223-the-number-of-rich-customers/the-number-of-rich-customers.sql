# Write your MySQL query statement below
select COUNT(customer_id) as rich_count from (select distinct customer_id from Store where amount > 500) as rich;