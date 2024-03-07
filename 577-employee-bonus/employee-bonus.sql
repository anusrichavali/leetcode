# Write your MySQL query statement below
Select Employee.name, Bonus.bonus From Employee LEFT JOIN Bonus ON Employee.empId = Bonus.empId Where Bonus.bonus < 1000 or Bonus.bonus IS NULL; 