-- this creates a table force_name with a default id of 1 and it is also unique
CREATE TABLE IF NOT EXISTS `unique_id`(`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256) NOT NULL);
