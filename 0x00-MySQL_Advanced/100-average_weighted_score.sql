-- Computes average score of a user and stores it
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN u_id INT)
BEGIN
	SELECT SUM((c.score * p.weight)) / SUM(p.weight)
	INTO @avg_score
	FROM corrections AS c 
	INNER JOIN projects AS p
	ON c.project_id = p.id WHERE c.user_id = u_id;

	UPDATE users SET average_score = @avg_score
	WHERE id = u_id;
END $$
DELIMITER ;

