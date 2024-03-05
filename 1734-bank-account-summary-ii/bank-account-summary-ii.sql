# Write your MySQL query statement below
Select name, SUM(amount) as balance FROM Users INNER JOIN Transactions ON Users.account = Transactions.account Group By name HAVING SUM(amount) > 10000;