-- Removes all records with a score below 6
UPDATE second_table DROP id, score, name WHERE score <= 5;
