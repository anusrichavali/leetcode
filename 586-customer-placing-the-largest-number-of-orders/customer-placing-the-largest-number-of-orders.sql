# Write your MySQL query statement below
Select customer_number FROM ORDERS Group BY customer_number Order BY COUNT(customer_number) DESC Limit 1;