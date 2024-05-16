# Write your MySQL query statement below
select f.id from weather f join weather l on datediff(f.recordDate, l.recordDate) = 1 where f.temperature > l.temperature;