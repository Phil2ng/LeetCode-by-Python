SELECT MAX(Salary) SecondHighestSalary
    FROM Employee
    WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee);  