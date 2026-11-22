/*
- Could be done with multiple self-joins 
  or
  LEAD() LAG() functions
*/

-- Using multiple self joins
/*
SELECT
    DISTINCT l1.num AS ConsecutiveNums
FROM
    Logs l1 
JOIN
    Logs l2
ON
    l1.id = (l2.id + 1) AND l1.num = l2.num
JOIN
    Logs l3
ON
    l1.id = (l3.id + 2) AND l1.num = l3.num
*/

-- using LAG function
SELECT
    DISTINCT num AS ConsecutiveNums
FROM
    (
        SELECT 
            num,
            LAG(num, 1) OVER (ORDER BY id) AS prev1,
            LAG(num, 2) OVER (ORDER BY id) AS prev2
        FROM
            Logs
    ) AS sub
WHERE num = prev1 AND num = prev2