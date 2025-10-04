SELECT w1.id
FROM Weather w1
JOIN Weather w 
  ON DATEDIFF(w1.recordDate, w.recordDate) = 1
WHERE w1.temperature > w.temperature;