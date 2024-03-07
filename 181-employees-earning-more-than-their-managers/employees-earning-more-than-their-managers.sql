# Write your MySQL query statement below
Select E1.name as Employee From Employee E1 Inner Join Employee E2 ON E1.managerID = E2.id where E1.salary > E2.salary