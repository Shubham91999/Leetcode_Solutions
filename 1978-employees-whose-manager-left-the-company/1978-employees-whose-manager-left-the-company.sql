/*
- IDs of employees with salary strictly less than 30000
- Whose manager left the company
- Both conditions should be met
- manager_id will not be present as employee_id in table
- Order by employee_id
*/

/*
SELECT 
    e1.employee_id
FROM
    Employees e1
LEFT JOIN
    Employees e2
ON
    e1.manager_id = e2.employee_id
WHERE 
    e1.salary < 30000 AND e2.employee_id IS null AND e1.manager_id IS NOT NULL
ORDER BY
    e1.employee_id
*/
-- Write your PostgreSQL query statement below
select
    employee_id
from
    Employees
where
    manager_id not in (
        select
            employee_id
        from
            Employees
    ) and salary < 30000
order by
    employee_id
