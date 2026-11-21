/*
- All sales occurred in first year each product was sold 
- For each product -> get the earliest year it was sold from Sales table
- Return all sales for that year for the product

- product_id, first_year, quantity, price

*/

SELECT 
    product_id, year AS first_year, quantity, price
FROM
    Sales
WHERE
    (product_id, year) IN (
    SELECT
        product_id,
        MIN(year) as first_year
    FROM
        Sales
    GROUP BY
        product_id)