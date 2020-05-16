DROP DATABASE IF EXISTS `sql_match_history`;
CREATE DATABASE `sql_match_history`; 
USE `sql_match_history`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE `Match_History` (
  `ID` tinyint(4) NOT NULL AUTO_INCREMENT,
  `Summoner_Name` varchar(10) NOT NULL,
  `Puuid` varchar(255) NOT NULL,
  `Match_History_ID` varchar(14) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;