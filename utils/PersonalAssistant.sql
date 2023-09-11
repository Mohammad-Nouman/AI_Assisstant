CREATE DATABASE PersonalAssistant;
use PersonalAssistant;


CREATE TABLE `PersonalAssistant`.`command` (
  `idCommand` INT NOT NULL,
  `fword` VARCHAR(100) NULL,
  `lword` VARCHAR(100) NULL,
  `detail` VARCHAR(1000) NULL,
  PRIMARY KEY (`idCommand`));
  
  INSERT INTO `PersonalAssistant`.`command`
 (`idCommand`,`fword`,`lword`,`detail`)
 VALUES(1,'create','screen','001');
 
 select * from command;