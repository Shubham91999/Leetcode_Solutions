/*
- Manager -> employee who has atleast 1 other employee reporting to them
- ids, name of manager, number of employees who report to them, avg age of reports 
- avg age rounded to integer
- order by employee_id
*/
SELECT 
    manager_id AS employee_id, name, reports_count, average_age
FROM
    Employees e1
JOIN
    (SELECT
        reports_to AS manager_id,
        COUNT(reports_to) AS reports_count,
        ROUND(AVG(age), 0) AS average_age
    FROM
        Employees
    WHERE 
        reports_to IS NOT NULL
    GROUP BY
        reports_to) as e2
ON
    e1.employee_id = e2.manager_id
ORDER BY
    employee_id

