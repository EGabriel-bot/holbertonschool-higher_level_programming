-- Number by score
-- lists the number of records with the same score in the table second_table
SELECT score, COUNT(score) as number from second_table GROUP BY score ORDER BY number DESC;
