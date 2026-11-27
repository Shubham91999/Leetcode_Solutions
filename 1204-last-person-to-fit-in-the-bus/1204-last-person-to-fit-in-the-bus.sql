/*
- n people to board the bus
- Weight limit of 1000
- find the last person to board the bus without exceeding the weight limit.

- Self join the table such that nth turn will be joined with n-1, n-2,... 1st turn row
- Total weight for turn n using SUM() 
- Limit till 1000, order by descending
- Return only first  

*/

SELECT 
    q1.person_name
FROM
    Queue q1
JOIN
    Queue q2
ON
    q1.turn >= q2.turn
GROUP BY
    q1.turn
HAVING 
    SUM(q2.weight) <= 1000
ORDER BY
    SUM(q2.weight) DESC
LIMIT 1
