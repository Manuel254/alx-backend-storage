-- Lists all bands with Glam rock as their main style ranked by longetivity
-- query
SELECT band_name, (COALESCE(split, 2022) - formed) as lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam Rock', style) <> 0
ORDER BY lifespan DESC
