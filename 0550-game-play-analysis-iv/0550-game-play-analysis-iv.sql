/*
- Fraction of players that logged in again on the day after the day they first logged in
- Rounded to 2 decimal
- Number of players logged in the next day from their intial login / Number of total players
*/

SELECT
    ROUND(SUM(event_date = DATE_ADD(first_login, INTERVAL 1 DAY)) / COUNT(DISTINCT player_id), 2) as fraction
FROM
    (SELECT
        player_id, event_date, 
        MIN(event_date) OVER (PARTITION BY player_id) AS first_login
    FROM
        Activity) AS t 