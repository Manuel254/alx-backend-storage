-- Computes average score of a user and stores it
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	SELECT AVG(score) INTO @avg_score FROM corrections
	WHERE user_id = user_id;
	UPDATE users SET average_score = @avg_score
	WHERE id = user_id;
END $$
DELIMITER ;

