# Write your MySQL query statement below
Select id, name From Students WHERE department_id NOT IN(Select id FROM Departments);