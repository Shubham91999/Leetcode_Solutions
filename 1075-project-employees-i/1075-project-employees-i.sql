/*
- Average exp years of all employees for each project 
- Rounded to 2 digits
- No order by
*/

SELECT
    p.project_id,
    -- SUM(e.experience_years) AS total_years,
    -- COUNT(*) AS total_employees,
    ROUND(SUM(e.experience_years)/COUNT(*), 2) AS average_years
FROM 
    Project p
JOIN
    Employee e
ON  
    p.employee_id = e.employee_id
GROUP BY
    p.project_id
