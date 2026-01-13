# Write your MySQL query statement below
SELECT e.name as Employee
FROM Employee as e
JOIN Employee as ea
ON  e.managerId = ea.id
where e.salary > ea.salary
