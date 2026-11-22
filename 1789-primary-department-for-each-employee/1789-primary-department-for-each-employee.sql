/*
- Employee can belong to multiple departments
- If emp belongs to only one department -> primary column in N
- All employees with their primary department
- Empl with only one department, report the same 
- No order
*/
/*
SELECT
    employee_id, department_id
FROM
    Employee
WHERE 
    primary_flag = 'Y'
UNION
SELECT 
    employee_id, department_id
FROM
    Employee
GROUP BY
    employee_id
HAVING 
    COUNT(*) = 1
*/
/*
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
        HAVING 
            COUNT(*) = 1
    )
*/
SELECT
    employee_id, department_id
FROM
    (SELECT
        *,
        COUNT(*) OVER (PARTITION BY employee_id) AS dept_count
    FROM
        Employee) AS sub
WHERE 
    primary_flag = 'Y' OR dept_count = 1
