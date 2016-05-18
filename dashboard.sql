-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dashboarddb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dashboarddb
-- -----------------------------------------------------
-- CREATE SCHEMA IF NOT EXISTS `dashboarddb` DEFAULT CHARACTER SET latin1 ;

-- -----------------------------------------------------
-- Table `dashboarddb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dashboard`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `permission` INT(11) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dashboarddb`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dashboard`.`messages` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `message` TEXT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `posted_id` INT(11) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users1_idx` (`posted_id` ASC),
  INDEX `fk_messages_users2_idx` (`user_id` ASC),
  CONSTRAINT `fk_messages_users1`
    FOREIGN KEY (`posted_id`)
    REFERENCES `dashboard`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_users2`
    FOREIGN KEY (`user_id`)
    REFERENCES `dashboard`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dashboard`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dashboard`.`comments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `comment` TEXT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `message_id` INT(11) NOT NULL,
  `user_id` INT(11) NOT NULL,
  `posted_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_messages_idx` (`message_id` ASC),
  INDEX `fk_comments_users1_idx` (`user_id` ASC),
  INDEX `fk_comments_users2_idx` (`posted_id` ASC),
  CONSTRAINT `fk_comments_messages`
    FOREIGN KEY (`message_id`)
    REFERENCES `dashboard`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `dashboard`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users2`
    FOREIGN KEY (`posted_id`)
    REFERENCES `dashboard`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
