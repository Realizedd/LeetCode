# Write your MySQL query statement below
select ifnull( (select distinct Employee.salary from Employee order by Employee.salary desc limit 1, 1), null) as SecondHighestSalary