/*
- 

*/
SELECT
    MAX(NUM) AS num
FROM
    (SELECT
        num 
    FROM
        MyNumbers
    GROUP BY
        num
    HAVING 
        COUNT(num) < 2) AS sub