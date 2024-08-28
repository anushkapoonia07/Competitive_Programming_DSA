# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# There are no different rows with the same recordDate.
# This table contains information about the temperature on a certain day.
 

# Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

# Return the result table in any order.

# The result format is in the following example.

# Problem Link: https://leetcode.com/problems/rising-temperature/description/

SELECT Today.id
FROM Weather AS Today
INNER JOIN Weather AS Yesterday
    ON (DATE_SUB(Today.recordDate, INTERVAL 1 DAY) = Yesterday.recordDate)
WHERE Today.temperature > Yesterday.temperature;