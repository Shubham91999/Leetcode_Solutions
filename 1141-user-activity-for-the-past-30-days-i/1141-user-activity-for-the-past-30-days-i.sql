/*
- Daily active user for a period of 30 days ending 2019-07-27 -> (2019-06-27 - 2019-07-27)
- User was active if they made any activity on that day 
- No order
*/

SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM
    Activity
WHERE
    activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY
    activity_date