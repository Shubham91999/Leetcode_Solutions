/*
- Addition of any two sides should not exceed the third side
- side 1 + side 2 <= side 3
- if any of the condition fails -> NO triangle
- if all true -> YES triangle
*/

SELECT
    x, y, z,
    IF(x+y <= z OR x+z <= y OR y+z <= x, 'No', 'Yes') AS triangle
FROM
    Triangle