DROP DATABASE IF EXISTS `sql_match_history`;
CREATE DATABASE `sql_match_history`; 
USE `sql_match_history`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE Match_History (
  ID tinyint(4) NOT NULL AUTO_INCREMENT,
  Summoner_Name varchar(10) NOT NULL,
  Puuid varchar(255) NOT NULL,
  Match_History_ID varchar(14) NOT NULL,
  PRIMARY KEY (ID),
  UNIQUE (Match_History_ID)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE Match_Data (
  Match_ID varchar(14) NOT NULL,
  End_Level tinyint(4) NOT NULL, 
  Placement tinyint(4) NOT NULL, 
  Primary_Trait varchar(25) NOT NULL, 
  Total_Damage tinyint(10) NOT NULL,
  PRIMARY KEY (Match_ID),
  FOREIGN KEY (Match_ID) REFERENCES Match_History (Match_History_ID) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;