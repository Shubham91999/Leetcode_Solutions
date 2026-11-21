/*
- Number of unique subjects each teacher teaches 
- No order

*/

SELECT 
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM
    Teacher
GROUP BY
    teacher_id
