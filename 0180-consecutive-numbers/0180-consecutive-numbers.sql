/*
- Return numbers that appear at least three times consecutively
- No order

- Self join can be used considering id doesn't have gaps
- LAG/LEAD window function -> deals with gaps, but needs rows present (max lag number + 1)
*/
SELECT
    DISTINCT t1.current_num AS ConsecutiveNums
FROM
    (SELECT
        num AS current_num,
        LEAD(num, 1) OVER (ORDER BY id) AS next1,
        LEAD(num, 2) OVER (ORDER BY id) AS next2
    FROM
        Logs) AS t1
WHERE 
    t1.current_num = t1.next1 AND t1.current_num = t1.next2