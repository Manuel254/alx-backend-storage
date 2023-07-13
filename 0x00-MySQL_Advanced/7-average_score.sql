-- Computes average score of a user and stores it
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN u_id INT)
BEGIN
	SELECT AVG(score) INTO @avg_score FROM corrections
	WHERE user_id = u_id;
	UPDATE users SET average_score = @avg_score
	WHERE id = u_id;
END $$
DELIMITER ;

