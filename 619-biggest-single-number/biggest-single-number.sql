# Write your MySQL query statement below
select max(num) as num from (Select m.num from MyNumbers m group by num having count(num) = 1) as single_numbers;