-- Computes average score of a user and stores it
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	SELECT SUM((c.score * p.weight)) / SUM(p.weight)
	INTO @avg_score
	FROM corrections AS c 
	INNER JOIN projects AS p
	ON c.project_id = p.id;

	UPDATE users SET average_score = @avg_score
END $$
DELIMITER ;

