/*
- Customer ids that bought all the products in Products tables
- No order

- Get the total number of products from Products table
- Get the total number of products bought by each customer with distinct product ids 
- Divide count of products bough / total products count for each customer
*/

SELECT
    customer_id
FROM
    customer
GROUP BY
    customer_id
HAVING 
    COUNT(DISTINCT product_key) = (SELECT COUNT(DISTINCT product_key) FROM Product)

