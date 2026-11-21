/*
- preferred delivery date = order date -> immediate
- preferred delivery date != order date -> scheduled

- Earliest order by customer -> first order

- percentage of immediate orders in first orders
- rounded to 2
- no order 

- Get first orders per customer 
- Check if those orders have same preferred delivery date = order date -> count of immediate -> count_immediate
- count of all first orders -> count_first
- count_immediate / count_first

*/
/*
SELECT
    ROUND(AVG(order_date = customer_pref_delivery_date)*100, 2) AS immediate_percentage
FROM
    Delivery
WHERE
    (customer_id, order_date) in (
                                    SELECT 
                                        customer_id, 
                                        MIN(order_date) AS order_date
                                    FROM
                                        Delivery
                                    GROUP BY
                                        customer_id
    )
*/
SELECT
    ROUND(AVG(order_date=customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM
    (SELECT
        *,
        RANK() OVER (PARTITION BY customer_id ORDER BY order_date) as rn
    FROM
        Delivery) as sub
WHERE 
    rn = 1
