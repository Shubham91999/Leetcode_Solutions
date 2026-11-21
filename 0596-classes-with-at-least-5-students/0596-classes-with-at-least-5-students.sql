/*
- Classes that have atleast 5 students
- No order
*/

SELECT
    class
FROM
    Courses
GROUP BY 
    class
HAVING 
    COUNT(DISTINCT student) >= 5