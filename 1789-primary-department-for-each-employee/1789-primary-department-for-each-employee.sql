/*
- Emp belongs to only one department -> primary column is N
- Return primary department for all employees  -> group by employee_id
- No order

*/

SELECT 
    employee_id, department_id
FROM
    Employee
WHERE
    primary_flag = 'Y' OR employee_id IN (
        SELECT 
            employee_id 
        FROM
            Employee
        GROUP BY
            employee_id
        HAVING COUNT(*) = 1
    )