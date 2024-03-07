# Write your MySQL query statement below
SELECT * from Salary s1 where salary = (Select MAX(salary) from SALARY s2 Where s1.emp_id = s2.emp_id) Order By emp_id ASC;