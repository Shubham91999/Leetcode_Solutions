/*
- Fraction of players that logged in again on the day after the day they first logged in
- Rounded to 2 decimal
- Number of players logged in the next day from their intial login / Number of total players
*/

SELECT
    -- *,
    -- SUM(CASE WHEN a1.event_date = DATE_ADD(a2.first_login, INTERVAL 1 DAY) THEN 1 ELSE 0 END),
    -- COUNT(DISTINCT a1.player_id),
    ROUND(SUM(CASE WHEN a1.event_date = DATE_ADD(a2.first_login, INTERVAL 1 DAY) THEN 1 ELSE 0 END) / COUNT(DISTINCT a1.player_id), 2) AS fraction

FROM
    Activity a1
JOIN
    (SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM
        Activity
    GROUP BY
        player_id) AS a2
ON 
    a1.player_id = a2.player_id
