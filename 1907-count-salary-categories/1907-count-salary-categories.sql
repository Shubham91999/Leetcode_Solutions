/*
- Low - strictly less than 20000
- Average - Between 20000 AND 50000
- High - Greater than 5000
- Return 0 if no accounts - COALESCE
- No order
*/


SELECT
    t1.category,
    COUNT(t2.category) AS accounts_count
FROM
    (SELECT 'Low Salary' AS category
    UNION ALL SELECT 'Average Salary' AS category
    UNION ALL SELECT 'High Salary' AS Category) AS t1
LEFT JOIN
    (SELECT 
        account_id,
        income,
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary'
        END AS category
    FROM
        Accounts) AS t2
ON 
    t1.category = t2.category
GROUP BY
    t1.category

