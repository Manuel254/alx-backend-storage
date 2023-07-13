-- ranks country origins of bands, ordered by the number of (non-unique) fans
-- check if index exists
SELECT COUNT(*)
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA 'holberton'
  AND TABLE_NAME = 'metal_bands'
  AND INDEX_NAME = 'origin_fan_count';
-- create an index for optimization
CREATE INDEX origin_fan_count ON metal_bands (origin, fans);

-- select only the origin column and fans column an order fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
