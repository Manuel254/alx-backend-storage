-- ranks country origins of bands, ordered by the number of (non-unique) fans
-- create an index for optimization
CREATE INDEX origin_fan_count ON metal_bands (id, origin, fans);

-- select only the origin column and fans column an order fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
