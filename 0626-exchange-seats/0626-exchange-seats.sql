/*
- swap the seat id of two consecutive students
- if total number of students is odd -> last one is not swapped
- Order by id ASC

*/

-- using IF 
SELECT
    IF(id < (SELECT MAX(id) FROM Seat), IF(id % 2 = 0, id-1, id+1), IF(id % 2 = 0, id-1, id)) AS id,
    student
FROM
    Seat
ORDER BY 
    id