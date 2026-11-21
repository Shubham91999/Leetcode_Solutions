/*
- Rating less than 3 -> poor query
- Query quality = query rating / position
- Poor query percentage = Queries with rating less than 3 / position 
- query_name, quality, poor_query_percentage
- Rounded away from zero, to 2 digits
- No order
*/

SELECT 
    query_name,
    ROUND(AVG(rating/position), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS poor_query_percentage
    
FROM
    Queries
GROUP BY
    query_name