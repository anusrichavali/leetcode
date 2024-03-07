# Write your MySQL query statement below
Select D1.id from Weather D1, Weather D2 WHERE D1.temperature > D2.temperature AND DateDiff(D1.recordDate, D2.recordDate) = 1;