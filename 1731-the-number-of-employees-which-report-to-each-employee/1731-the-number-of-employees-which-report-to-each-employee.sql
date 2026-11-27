/*
- employee_id -> primary key 
- Manager -> atleast 1 emp reporting to them
- Return id, manager name, number of reportees, average age of reportees (rounded to nearest integer)
- Order by employee_id

- Manager id can be derived from reports_to column -> use distinct
- name for that id from self join
- group by reports_to -> count -> reports_count
- group by reports_to -> avg of age -> average-age

*/
SELECT 
    t2.manager_id AS employee_id,
    t1.name,
    t2.reports_count,
    t2.average_age
FROM 
    Employees t1
JOIN
    (SELECT 
        reports_to AS manager_id,
        COUNT(*) AS reports_count,
        ROUND(AVG(age), 0) AS average_age
    FROM
        Employees
    GROUP BY
        reports_to) AS t2
ON 
    t1.employee_id = t2.manager_id
ORDER BY
    t1.employee_id 
