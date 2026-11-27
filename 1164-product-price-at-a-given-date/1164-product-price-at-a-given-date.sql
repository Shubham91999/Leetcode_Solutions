/*
- By default price 10
- find prices of all products (group by product) on date 2019-08-16
- No order


*/
SELECT
    p1.product_id,
    COALESCE(p2.price, 10) AS price
FROM
    Products p1
LEFT JOIN
    (SELECT
        product_id,
        new_price AS price,
        change_date,
        RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) as rn
    FROM
        Products
    WHERE
        change_date <= '2019-08-16') AS p2
ON 
    p1.product_id = p2.product_id AND p2.rn = 1
GROUP BY
    product_id


