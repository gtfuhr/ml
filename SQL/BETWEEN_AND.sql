SELECT *
FROM orders
WHERE standard_qty > 1000 AND poster_qty = 0 AND gloss_qty = 0;

-- Using the accounts table, find all the companies whose names do not start with 'C' and end with 's'.
SELECT name
FROM accounts
WHERE name NOT LIKE 'C%' AND name LIKE '%s';
-- When you use the BETWEEN operator in SQL, do the results include the values of your endpoints, or not? Figure out the answer to this important question by writing a query that displays the order date and gloss_qty data for all orders where gloss_qty is between 24 and 29. Then look at your output to see if the BETWEEN operator included the begin and end values or not.
SELECT occurred_at, gloss_qty 
FROM orders
WHERE gloss_qty BETWEEN 24 AND 29;