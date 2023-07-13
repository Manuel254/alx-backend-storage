-- Lists all bands with Glam rock as their main style ranked by longetivity
-- query
SELECT band_name, (split - formed) as lifespan
FROM metal_bands
WHERE split <= 2022
AND style="Glam rock"
ORDER BY lifespan DESC
