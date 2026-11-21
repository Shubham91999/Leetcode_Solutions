/*
- All sales occurred in first year each product was sold 
- For each product -> get the earliest year it was sold from Sales table
- Return all sales for that year for the product

- product_id, first_year, quantity, price

*/
SELECT
    product_id, year AS first_year, quantity, price
FROM
    (SELECT
        *,
        RANK() OVER (PARTITION BY product_id ORDER BY year) as rn
    FROM
        Sales) as sub
WHERE rn = 1