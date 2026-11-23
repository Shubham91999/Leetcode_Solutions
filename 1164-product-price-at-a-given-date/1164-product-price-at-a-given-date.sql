/*
- All products have price 10 initially
- Find: prices of all producst on date 2019-08-16
- No order
*/
SELECT 
    DISTINCT p.product_id,
    COALESCE(sub.new_price, 10) AS price
FROM
    Products p
LEFT JOIN
    (SELECT
        *,
        RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM
        Products
    WHERE 
        change_date <= '2019-08-16') AS sub
ON
    p.product_id = sub.product_id AND sub.rn = 1
