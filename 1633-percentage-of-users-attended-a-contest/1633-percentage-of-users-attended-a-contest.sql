/*
- Percentage of users registered in each contest
- users registered for contest / total number of users
- Rounded to 2
- Order by percentage DESC, contest_id ASC
*/

SELECT 
    contest_id, 
    ROUND(COUNT(*) / (
                SELECT 
                    COUNT(DISTINCT user_id) AS total_users
                FROM 
                    Users
                    )*100, 2) AS percentage
FROM
    Register
GROUP BY
    contest_id
ORDER BY
    percentage DESC, contest_id ASC



