# Write your MySQL query statement below
Select name as Customers From Customers WHERE Customers.id NOT IN(Select customerId from Orders);