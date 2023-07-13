-- Creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	SELECT COUNT(*) INTO @proj_exist FROM projects WHERE name = project_name;

	IF @proj_exist = 0 THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;

	SELECT id INTO @project_id FROM projects WHERE name = project_name;
	INSERT INTO corrections VALUES (user_id, @project_id, score);
END $$
DELIMITER ;
