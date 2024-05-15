# Write your MySQL query statement below
select distinct c.class from courses c where (select count(*) from courses c2 where c.class = c2.class group by class) >= 5;