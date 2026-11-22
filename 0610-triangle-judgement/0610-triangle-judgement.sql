/*
- if x + y > z / x + z > y / y + z > x
- Any of them is true -> triangle

*/

SELECT
    x, y, z,
    CASE WHEN x+y>z AND x+z>y AND y+z>x THEN 'Yes' ELSE 'No' END AS triangle
FROM
    Triangle