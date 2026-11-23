/*
- turn = 1 -> first person to board the bus
- turn = n -> last person to board
- bus has weight limit -> 1000
- Find person_name of last paerson to board the bus
*/

SELECT
    a.person_name
FROM
    Queue a
JOIN
    Queue b
ON
    a.turn >= b.turn
GROUP BY
    a.turn
HAVING 
    SUM(b.weight) <= 1000
ORDER BY
    SUM(b.weight) DESC
LIMIT 1
