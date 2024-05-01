-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: church_db
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BAPTISM`
--

DROP TABLE IF EXISTS `BAPTISM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BAPTISM` (
  `BAPTISM_ID` varchar(255) NOT NULL,
  `BAPTISM_NO` int DEFAULT NULL,
  `G_CHILD` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `MOTHER_ID` varchar(255) DEFAULT NULL,
  `FATHER_ID` varchar(255) DEFAULT NULL,
  `BAPTISM_AT` varchar(255) DEFAULT NULL,
  `g_PERSONS_ID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`BAPTISM_ID`),
  KEY `MOTHER_ID` (`MOTHER_ID`),
  KEY `FATHER_ID` (`FATHER_ID`),
  KEY `BAPTISM_AT` (`BAPTISM_AT`),
  KEY `g_PERSONS_ID` (`g_PERSONS_ID`),
  KEY `G_CHILD` (`G_CHILD`),
  CONSTRAINT `BAPTISM_ibfk_1` FOREIGN KEY (`MOTHER_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `BAPTISM_ibfk_2` FOREIGN KEY (`FATHER_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `BAPTISM_ibfk_3` FOREIGN KEY (`BAPTISM_AT`) REFERENCES `LOCATION` (`LOCATION_ID`),
  CONSTRAINT `BAPTISM_ibfk_4` FOREIGN KEY (`g_PERSONS_ID`) REFERENCES `G_PERSONS` (`G_PERSONS_ID`),
  CONSTRAINT `BAPTISM_ibfk_5` FOREIGN KEY (`G_CHILD`) REFERENCES `PERSONS` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BAPTISM`
--

LOCK TABLES `BAPTISM` WRITE;
/*!40000 ALTER TABLE `BAPTISM` DISABLE KEYS */;
INSERT INTO `BAPTISM` VALUES ('1182e533-060e-11ef-8423-766bb54b59da',2342,'1182b997-060e-11ef-8423-766bb54b59da','1182ce47-060e-11ef-8423-766bb54b59da','1182d590-060e-11ef-8423-766bb54b59da',NULL,NULL),('29ce2977-060e-11ef-8423-766bb54b59da',2342,'29ce0be7-060e-11ef-8423-766bb54b59da','29ce1e6f-060e-11ef-8423-766bb54b59da','29ce22d5-060e-11ef-8423-766bb54b59da',NULL,NULL),('2a3d322f-03f8-11ef-bd7c-6b3ae1bc0afb',3414,'2a3d1bd2-03f8-11ef-bd7c-6b3ae1bc0afb','2a3d24a3-03f8-11ef-bd7c-6b3ae1bc0afb','2a3d296f-03f8-11ef-bd7c-6b3ae1bc0afb',NULL,NULL),('6c076ea4-060d-11ef-8423-766bb54b59da',3414,'6bfb2753-060d-11ef-8423-766bb54b59da','6bfbb6c2-060d-11ef-8423-766bb54b59da','6bfbd6f8-060d-11ef-8423-766bb54b59da',NULL,'6bfc599c-060d-11ef-8423-766bb54b59da'),('73938e70-d8aa-11ee-8d30-dd530a390159',3848,'7393328c-d8aa-11ee-8d30-dd530a390159','73937708-d8aa-11ee-8d30-dd530a390159','73937f35-d8aa-11ee-8d30-dd530a390159',NULL,NULL),('74743c85-d8b0-11ee-8d30-dd530a390159',232,'7465c728-d8b0-11ee-8d30-dd530a390159','7465f18b-d8b0-11ee-8d30-dd530a390159','74661260-d8b0-11ee-8d30-dd530a390159',NULL,'74664d98-d8b0-11ee-8d30-dd530a390159'),('856b1704-03fa-11ef-bd7c-6b3ae1bc0afb',3414,'856a8a17-03fa-11ef-bd7c-6b3ae1bc0afb','856aa530-03fa-11ef-bd7c-6b3ae1bc0afb','856ab870-03fa-11ef-bd7c-6b3ae1bc0afb',NULL,'856b0022-03fa-11ef-bd7c-6b3ae1bc0afb'),('96c5daad-d8b1-11ee-8d30-dd530a390159',222,'96c54bcf-d8b1-11ee-8d30-dd530a390159','96c559d0-d8b1-11ee-8d30-dd530a390159','96c55f91-d8b1-11ee-8d30-dd530a390159',NULL,'96c571d2-d8b1-11ee-8d30-dd530a390159');
/*!40000 ALTER TABLE `BAPTISM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CLAN`
--

DROP TABLE IF EXISTS `CLAN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CLAN` (
  `CID` varchar(255) NOT NULL,
  `TRIBE_ID` varchar(255) DEFAULT NULL,
  `CLAN_NAME` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`CID`),
  KEY `TRIBE_ID` (`TRIBE_ID`),
  CONSTRAINT `CLAN_ibfk_1` FOREIGN KEY (`TRIBE_ID`) REFERENCES `TRIBE` (`TRIBE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CLAN`
--

LOCK TABLES `CLAN` WRITE;
/*!40000 ALTER TABLE `CLAN` DISABLE KEYS */;
INSERT INTO `CLAN` VALUES ('0f69ca04-025a-11ef-b482-37e2c534b4eb','91e4914f-d73b-11ee-8358-94b86de0e66a','kilimoal'),('6482dc75-0587-11ef-962a-94b86de0e66a','91e4914f-d73b-11ee-8358-94b86de0e66a','MOSTLALI'),('71348d02-024d-11ef-921e-94b86de0e66a','91e4914f-d73b-11ee-8358-94b86de0e66a','valamu'),('83239e3a-024e-11ef-921e-94b86de0e66a','91e4914f-d73b-11ee-8358-94b86de0e66a','ilumo'),('b9e6ad31-0589-11ef-962a-94b86de0e66a','91e4914f-d73b-11ee-8358-94b86de0e66a','AVOUT LAM'),('d728dfed-0314-11ef-a060-94b86de0e66a','91e4914f-d73b-11ee-8358-94b86de0e66a','MOSALI');
/*!40000 ALTER TABLE `CLAN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CONFIRMATION`
--

DROP TABLE IF EXISTS `CONFIRMATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CONFIRMATION` (
  `CONFIMARTION_ID` varchar(255) NOT NULL,
  `CONFIMATION_NO` int DEFAULT NULL,
  `DATE_` date DEFAULT NULL,
  `PID` varchar(255) DEFAULT NULL,
  `MOTHER_ID` varchar(255) DEFAULT NULL,
  `FATHER_ID` varchar(255) DEFAULT NULL,
  `NO_MEN_BAPT` int DEFAULT NULL,
  `g_PERSONS_ID` varchar(255) DEFAULT NULL,
  `PRIEST_ID` varchar(255) DEFAULT NULL,
  `BAPTUM_DIE` varchar(50) DEFAULT NULL,
  `AT` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`CONFIMARTION_ID`),
  KEY `PID` (`PID`),
  KEY `MOTHER_ID` (`MOTHER_ID`),
  KEY `FATHER_ID` (`FATHER_ID`),
  KEY `g_PERSONS_ID` (`g_PERSONS_ID`),
  KEY `PRIEST_ID` (`PRIEST_ID`),
  KEY `AT` (`AT`),
  CONSTRAINT `CONFIRMATION_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `CONFIRMATION_ibfk_2` FOREIGN KEY (`MOTHER_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `CONFIRMATION_ibfk_3` FOREIGN KEY (`FATHER_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `CONFIRMATION_ibfk_4` FOREIGN KEY (`g_PERSONS_ID`) REFERENCES `G_PERSONS` (`G_PERSONS_ID`),
  CONSTRAINT `CONFIRMATION_ibfk_5` FOREIGN KEY (`PRIEST_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `CONFIRMATION_ibfk_6` FOREIGN KEY (`AT`) REFERENCES `LOCATION` (`LOCATION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CONFIRMATION`
--

LOCK TABLES `CONFIRMATION` WRITE;
/*!40000 ALTER TABLE `CONFIRMATION` DISABLE KEYS */;
/*!40000 ALTER TABLE `CONFIRMATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COUPLES`
--

DROP TABLE IF EXISTS `COUPLES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `COUPLES` (
  `C_MEMBER_ID` varchar(255) NOT NULL,
  `MARRIAGE_ID` varchar(255) DEFAULT NULL,
  `PERSON_ID` varchar(255) DEFAULT NULL,
  `MOTHER_ID` varchar(255) DEFAULT NULL,
  `FATHER_ID` varchar(255) DEFAULT NULL,
  `BAPTISM` varchar(255) DEFAULT NULL,
  `DOMICILE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`C_MEMBER_ID`),
  KEY `MARRIAGE_ID` (`MARRIAGE_ID`),
  KEY `PERSON_ID` (`PERSON_ID`),
  KEY `MOTHER_ID` (`MOTHER_ID`),
  KEY `FATHER_ID` (`FATHER_ID`),
  KEY `BAPTISM` (`BAPTISM`),
  CONSTRAINT `COUPLES_ibfk_1` FOREIGN KEY (`MARRIAGE_ID`) REFERENCES `MARRIAGE_` (`MARRIAGE_ID`),
  CONSTRAINT `COUPLES_ibfk_2` FOREIGN KEY (`PERSON_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `COUPLES_ibfk_3` FOREIGN KEY (`MOTHER_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `COUPLES_ibfk_4` FOREIGN KEY (`FATHER_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `COUPLES_ibfk_5` FOREIGN KEY (`BAPTISM`) REFERENCES `BAPTISM` (`BAPTISM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COUPLES`
--

LOCK TABLES `COUPLES` WRITE;
/*!40000 ALTER TABLE `COUPLES` DISABLE KEYS */;
/*!40000 ALTER TABLE `COUPLES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEATH`
--

DROP TABLE IF EXISTS `DEATH`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DEATH` (
  `DEATH_ID` varchar(255) NOT NULL,
  `DEATH_NO` int DEFAULT NULL,
  `PID` varchar(255) DEFAULT NULL,
  `SO_OR_DO` varchar(50) DEFAULT NULL,
  `DISTRICT_ID` varchar(255) DEFAULT NULL,
  `BAPTISM_ID` varchar(255) DEFAULT NULL,
  `MARRIAGE_ID` varchar(255) DEFAULT NULL,
  `last_rite` enum('YES','NO') DEFAULT NULL,
  `BURIAL_PLACE` varchar(255) DEFAULT NULL,
  `BURIAL_DATE` date DEFAULT NULL,
  `priest_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`DEATH_ID`),
  KEY `PID` (`PID`),
  KEY `DISTRICT_ID` (`DISTRICT_ID`),
  KEY `BAPTISM_ID` (`BAPTISM_ID`),
  KEY `MARRIAGE_ID` (`MARRIAGE_ID`),
  KEY `BURIAL_PLACE` (`BURIAL_PLACE`),
  KEY `priest_id` (`priest_id`),
  CONSTRAINT `DEATH_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `DEATH_ibfk_2` FOREIGN KEY (`DISTRICT_ID`) REFERENCES `LOCATION` (`LOCATION_ID`),
  CONSTRAINT `DEATH_ibfk_3` FOREIGN KEY (`BAPTISM_ID`) REFERENCES `BAPTISM` (`BAPTISM_ID`),
  CONSTRAINT `DEATH_ibfk_4` FOREIGN KEY (`MARRIAGE_ID`) REFERENCES `MARRIAGE_` (`MARRIAGE_ID`),
  CONSTRAINT `DEATH_ibfk_5` FOREIGN KEY (`BURIAL_PLACE`) REFERENCES `LOCATION` (`LOCATION_ID`),
  CONSTRAINT `DEATH_ibfk_6` FOREIGN KEY (`priest_id`) REFERENCES `PERSONS` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEATH`
--

LOCK TABLES `DEATH` WRITE;
/*!40000 ALTER TABLE `DEATH` DISABLE KEYS */;
/*!40000 ALTER TABLE `DEATH` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DISPENSATION`
--

DROP TABLE IF EXISTS `DISPENSATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DISPENSATION` (
  `DISP_ID` varchar(255) NOT NULL,
  `MARRIAGE_ID` varchar(255) DEFAULT NULL,
  `D_FROM` varchar(50) DEFAULT NULL,
  `GIVEN_BY` varchar(50) DEFAULT NULL,
  `EMPEPIMENTS_OF` varchar(50) DEFAULT NULL,
  `DATE_` date DEFAULT NULL,
  `LOCATION_ID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`DISP_ID`),
  KEY `MARRIAGE_ID` (`MARRIAGE_ID`),
  KEY `LOCATION_ID` (`LOCATION_ID`),
  CONSTRAINT `DISPENSATION_ibfk_1` FOREIGN KEY (`MARRIAGE_ID`) REFERENCES `MARRIAGE_` (`MARRIAGE_ID`),
  CONSTRAINT `DISPENSATION_ibfk_2` FOREIGN KEY (`LOCATION_ID`) REFERENCES `LOCATION` (`LOCATION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DISPENSATION`
--

LOCK TABLES `DISPENSATION` WRITE;
/*!40000 ALTER TABLE `DISPENSATION` DISABLE KEYS */;
/*!40000 ALTER TABLE `DISPENSATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `G_PERSONS`
--

DROP TABLE IF EXISTS `G_PERSONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `G_PERSONS` (
  `G_PERSONS_ID` varchar(255) NOT NULL,
  `G_FATHER` varchar(255) DEFAULT NULL,
  `S_O_father` varchar(50) DEFAULT NULL,
  `G_MOTHER` varchar(255) DEFAULT NULL,
  `S_O_mother` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`G_PERSONS_ID`),
  KEY `G_FATHER` (`G_FATHER`),
  KEY `G_MOTHER` (`G_MOTHER`),
  CONSTRAINT `G_PERSONS_ibfk_1` FOREIGN KEY (`G_FATHER`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `G_PERSONS_ibfk_2` FOREIGN KEY (`G_MOTHER`) REFERENCES `PERSONS` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `G_PERSONS`
--

LOCK TABLES `G_PERSONS` WRITE;
/*!40000 ALTER TABLE `G_PERSONS` DISABLE KEYS */;
INSERT INTO `G_PERSONS` VALUES ('6bfc599c-060d-11ef-8423-766bb54b59da','6bfc1fae-060d-11ef-8423-766bb54b59da','mosr','6bfc39f1-060d-11ef-8423-766bb54b59da','javal'),('74664d98-d8b0-11ee-8d30-dd530a390159','74662e1f-d8b0-11ee-8d30-dd530a390159','null','74663e90-d8b0-11ee-8d30-dd530a390159','null'),('856b0022-03fa-11ef-bd7c-6b3ae1bc0afb','856ad22b-03fa-11ef-bd7c-6b3ae1bc0afb','mosr','856aea09-03fa-11ef-bd7c-6b3ae1bc0afb','javal'),('96c571d2-d8b1-11ee-8d30-dd530a390159','96c56554-d8b1-11ee-8d30-dd530a390159','null','96c56b62-d8b1-11ee-8d30-dd530a390159','null');
/*!40000 ALTER TABLE `G_PERSONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LOCATION`
--

DROP TABLE IF EXISTS `LOCATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LOCATION` (
  `LOCATION_ID` varchar(255) NOT NULL,
  `LOC_NAME` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`LOCATION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LOCATION`
--

LOCK TABLES `LOCATION` WRITE;
/*!40000 ALTER TABLE `LOCATION` DISABLE KEYS */;
/*!40000 ALTER TABLE `LOCATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MARRIAGE_`
--

DROP TABLE IF EXISTS `MARRIAGE_`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MARRIAGE_` (
  `MARRIAGE_ID` varchar(255) NOT NULL,
  `DATE_` date DEFAULT NULL,
  `CHURCH_OF` varchar(50) DEFAULT NULL,
  `BANNS_NO` int DEFAULT NULL,
  `DELEGATE_` varchar(255) DEFAULT NULL,
  `PRIEST_ID` varchar(255) DEFAULT NULL,
  `MALE_WITNESS_ID` varchar(255) DEFAULT NULL,
  `FEMALE_WITNESS_ID` varchar(255) DEFAULT NULL,
  `M_CERT_NO` int DEFAULT NULL,
  PRIMARY KEY (`MARRIAGE_ID`),
  KEY `PRIEST_ID` (`PRIEST_ID`),
  KEY `MALE_WITNESS_ID` (`MALE_WITNESS_ID`),
  KEY `FEMALE_WITNESS_ID` (`FEMALE_WITNESS_ID`),
  KEY `DELEGATE_` (`DELEGATE_`),
  CONSTRAINT `MARRIAGE__ibfk_2` FOREIGN KEY (`PRIEST_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `MARRIAGE__ibfk_3` FOREIGN KEY (`MALE_WITNESS_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `MARRIAGE__ibfk_4` FOREIGN KEY (`FEMALE_WITNESS_ID`) REFERENCES `PERSONS` (`PID`),
  CONSTRAINT `MARRIAGE__ibfk_5` FOREIGN KEY (`DELEGATE_`) REFERENCES `PERSONS` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MARRIAGE_`
--

LOCK TABLES `MARRIAGE_` WRITE;
/*!40000 ALTER TABLE `MARRIAGE_` DISABLE KEYS */;
INSERT INTO `MARRIAGE_` VALUES ('062ccc58-0721-11ef-8e0e-94b86de0e66a','2012-03-06','malatis',234234,'062c8551-0721-11ef-8e0e-94b86de0e66a','062ca408-0721-11ef-8e0e-94b86de0e66a','062cb297-0721-11ef-8e0e-94b86de0e66a','062cbedc-0721-11ef-8e0e-94b86de0e66a',234123),('1233232e-0721-11ef-8e0e-94b86de0e66a','1954-02-23','longont',2342,'1232f532-0721-11ef-8e0e-94b86de0e66a','123301e0-0721-11ef-8e0e-94b86de0e66a','12330ab7-0721-11ef-8e0e-94b86de0e66a','123316f6-0721-11ef-8e0e-94b86de0e66a',232),('7e470747-d8be-11ee-8d30-dd530a390159','2024-03-02',NULL,32342,'7e46ee09-d8be-11ee-8d30-dd530a390159','7e46f807-d8be-11ee-8d30-dd530a390159','7e46fcd8-d8be-11ee-8d30-dd530a390159','7e470193-d8be-11ee-8d30-dd530a390159',23424),('a3500e72-0720-11ef-8e0e-94b86de0e66a','2012-03-06','malatis',234234,'a34fdf69-0720-11ef-8e0e-94b86de0e66a','a34ff60d-0720-11ef-8e0e-94b86de0e66a','a34ffca7-0720-11ef-8e0e-94b86de0e66a','a350026a-0720-11ef-8e0e-94b86de0e66a',234123),('c2bdac61-d8bd-11ee-8d30-dd530a390159','2024-03-02',NULL,32342,'c2bd83b7-d8bd-11ee-8d30-dd530a390159','c2bd948d-d8bd-11ee-8d30-dd530a390159','c2bd9c09-d8bd-11ee-8d30-dd530a390159','c2bda272-d8bd-11ee-8d30-dd530a390159',23424),('c8adfed9-0714-11ef-8e0e-94b86de0e66a','2012-03-06','malatis',234234,'c895aaf2-0714-11ef-8e0e-94b86de0e66a','c8adc826-0714-11ef-8e0e-94b86de0e66a','c8add1c3-0714-11ef-8e0e-94b86de0e66a','c8adddc6-0714-11ef-8e0e-94b86de0e66a',234123),('cef87039-0727-11ef-9a90-2f2838a388bf','1954-02-23','longont',2342,'ceeca21c-0727-11ef-9a90-2f2838a388bf','cef85630-0727-11ef-9a90-2f2838a388bf','cef85aff-0727-11ef-9a90-2f2838a388bf','cef85e4b-0727-11ef-9a90-2f2838a388bf',232),('d82e6126-d8be-11ee-8d30-dd530a390159','2024-03-02',NULL,32342,'d82e4760-d8be-11ee-8d30-dd530a390159','d82e5312-d8be-11ee-8d30-dd530a390159','d82e571b-d8be-11ee-8d30-dd530a390159','d82e5c0c-d8be-11ee-8d30-dd530a390159',23424),('e5f68185-d8be-11ee-8d30-dd530a390159','2024-03-02',NULL,32342,'e5f659f8-d8be-11ee-8d30-dd530a390159','e5f66749-d8be-11ee-8d30-dd530a390159','e5f67198-d8be-11ee-8d30-dd530a390159','e5f67a43-d8be-11ee-8d30-dd530a390159',23424),('e75fd4ed-0727-11ef-9a90-2f2838a388bf','1954-02-23','longont',2342,'e75fb89e-0727-11ef-9a90-2f2838a388bf','e75fc73b-0727-11ef-9a90-2f2838a388bf','e75fcb3e-0727-11ef-9a90-2f2838a388bf','e75fcee7-0727-11ef-9a90-2f2838a388bf',232);
/*!40000 ALTER TABLE `MARRIAGE_` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PERSONS`
--

DROP TABLE IF EXISTS `PERSONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PERSONS` (
  `PID` varchar(255) NOT NULL,
  `FIRST_NAME` varchar(50) DEFAULT NULL,
  `LAST_NAME` varchar(50) DEFAULT NULL,
  `DATE_OF_BIRTH` date DEFAULT NULL,
  `TYPE` enum('P','N') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'N',
  `GENDER` enum('MALE','FEMALE') NOT NULL,
  `CLAN_ID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`PID`),
  KEY `CLAN_ID` (`CLAN_ID`),
  CONSTRAINT `PERSONS_ibfk_1` FOREIGN KEY (`CLAN_ID`) REFERENCES `CLAN` (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PERSONS`
--

LOCK TABLES `PERSONS` WRITE;
/*!40000 ALTER TABLE `PERSONS` DISABLE KEYS */;
INSERT INTO `PERSONS` VALUES ('062c8551-0721-11ef-8e0e-94b86de0e66a','deligateI','amos','2003-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('062ca408-0721-11ef-8e0e-94b86de0e66a','witness','SUfaU','2019-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('062cb297-0721-11ef-8e0e-94b86de0e66a','witness 2','valie','2013-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('062cbedc-0721-11ef-8e0e-94b86de0e66a','priest','VALUd','1976-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('1182b997-060e-11ef-8423-766bb54b59da','JOSE','OMARI','2004-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('1182ce47-060e-11ef-8423-766bb54b59da','BAKIJ','vOLLIA','1994-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('1182d590-060e-11ef-8423-766bb54b59da','loki','ramadh','1984-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('1232f532-0721-11ef-8e0e-94b86de0e66a','lakipata','omosta','1934-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('123301e0-0721-11ef-8e0e-94b86de0e66a','valimolit','olamina','1964-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('12330ab7-0721-11ef-8e0e-94b86de0e66a','omarival','kaptivi','2003-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('123316f6-0721-11ef-8e0e-94b86de0e66a','kaplatm','odowari','2003-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('22d8db6b-03f1-11ef-bd7c-6b3ae1bc0afb','MOVATI','SUMON VALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('234215123252','VAlkaN KACA','kilivalie MOSTA ','2024-02-29','P','MALE',NULL),('29ce0be7-060e-11ef-8423-766bb54b59da','JOSE','OMARI','2004-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('29ce1e6f-060e-11ef-8423-766bb54b59da','BAKIJ','vOLLIA','1994-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('29ce22d5-060e-11ef-8423-766bb54b59da','loki','ramadh','1984-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('2a3d1bd2-03f8-11ef-bd7c-6b3ae1bc0afb','MVATI','SUM VALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('2a3d24a3-03f8-11ef-bd7c-6b3ae1bc0afb','MOdVATI','SUM VALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('2a3d296f-03f8-11ef-bd7c-6b3ae1bc0afb','MOVdaATI','SUMON daVALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('324352','VAlkan father','kilivalie father','2024-02-29','P','MALE',NULL),('51b8525f-d8be-11ee-8d30-dd530a390159','inserted_me',' mostelt ','2024-02-29','N','FEMALE',NULL),('5acac0dc-d8be-11ee-8d30-dd530a390159','inserted_me',' mostelt ','2024-02-29','N','FEMALE',NULL),('5ba816b6-d8be-11ee-8d30-dd530a390159','inserted_me',' mostelt ','2024-02-29','N','FEMALE',NULL),('6bfb2753-060d-11ef-8423-766bb54b59da','MVATI','SUM VALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('6bfbb6c2-060d-11ef-8423-766bb54b59da','MOdVATI','SUM VALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('6bfbd6f8-060d-11ef-8423-766bb54b59da','MOVdaATI','SUMON daVALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('6bfc1fae-060d-11ef-8423-766bb54b59da','MOafaaATI','SbaaVALU','1993-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('6bfc39f1-060d-11ef-8423-766bb54b59da','gmother','valie VALU','2000-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('7393328c-d8aa-11ee-8d30-dd530a390159','MOSTVAL','ketheline','2024-02-29','P','MALE',NULL),('73937708-d8aa-11ee-8d30-dd530a390159',' jambo mother','kilide mother','2024-02-29','P','FEMALE',NULL),('73937f35-d8aa-11ee-8d30-dd530a390159','sfaAlkan father','kilidsevalie father','2024-02-29','P','MALE',NULL),('7465c728-d8b0-11ee-8d30-dd530a390159','JANETE','OUTEHR','2024-02-29','P','FEMALE',NULL),('7465f18b-d8b0-11ee-8d30-dd530a390159',' ROSEMARY ','MOSLY','2024-02-29','P','FEMALE',NULL),('74661260-d8b0-11ee-8d30-dd530a390159','JACOBA','KIMALI','2024-02-29','P','MALE',NULL),('74662e1f-d8b0-11ee-8d30-dd530a390159','mosess ','valuena val','2024-02-29','P','MALE',NULL),('74663e90-d8b0-11ee-8d30-dd530a390159','sharon','kisla','2024-02-29','P','FEMALE',NULL),('7e46ee09-d8be-11ee-8d30-dd530a390159','valen bona','kiproteach','2004-05-02','N','MALE',NULL),('7e46f807-d8be-11ee-8d30-dd530a390159','valuesvas','kiptoo','2024-05-02','N','MALE',NULL),('7e46fcd8-d8be-11ee-8d30-dd530a390159','mostal','usasalS','2020-03-02','N','MALE',NULL),('7e470193-d8be-11ee-8d30-dd530a390159','janete','kilapan','2002-03-02','N','FEMALE',NULL),('856a8a17-03fa-11ef-bd7c-6b3ae1bc0afb','MVATI','SUM VALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('856aa530-03fa-11ef-bd7c-6b3ae1bc0afb','MOdVATI','SUM VALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('856ab870-03fa-11ef-bd7c-6b3ae1bc0afb','MOVdaATI','SUMON daVALU','2023-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('856ad22b-03fa-11ef-bd7c-6b3ae1bc0afb','MOafaaATI','SbaaVALU','1993-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('856aea09-03fa-11ef-bd7c-6b3ae1bc0afb','gmother','valie VALU','2000-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('96c54bcf-d8b1-11ee-8d30-dd530a390159','ANETE','SOUTEHR','2024-02-29','N','FEMALE',NULL),('96c559d0-d8b1-11ee-8d30-dd530a390159',' ROSE ','SALLY','2024-02-29','N','FEMALE',NULL),('96c55f91-d8b1-11ee-8d30-dd530a390159','JACO','KIMAI','2024-02-29','N','MALE',NULL),('96c56554-d8b1-11ee-8d30-dd530a390159','mose ','value','2024-02-29','N','MALE',NULL),('96c56b62-d8b1-11ee-8d30-dd530a390159','aronA','islaSA','2024-02-29','N','MALE',NULL),('a34fdf69-0720-11ef-8e0e-94b86de0e66a','deligateI','amos','2003-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('a34ff60d-0720-11ef-8e0e-94b86de0e66a','witness','SUfaU','2019-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('a34ffca7-0720-11ef-8e0e-94b86de0e66a','witness 2','valie','2013-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('a350026a-0720-11ef-8e0e-94b86de0e66a','priest','VALUd','1976-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('c2bd83b7-d8bd-11ee-8d30-dd530a390159','valen bona','kiproteach','2004-05-02','N','MALE',NULL),('c2bd948d-d8bd-11ee-8d30-dd530a390159','valuesvas','kiptoo','2024-05-02','N','MALE',NULL),('c2bd9c09-d8bd-11ee-8d30-dd530a390159','mostal','usasalS','2020-03-02','N','MALE',NULL),('c2bda272-d8bd-11ee-8d30-dd530a390159','janete','kilapan','2002-03-02','N','FEMALE',NULL),('c895aaf2-0714-11ef-8e0e-94b86de0e66a','deligateI','amos','2003-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('c8adc826-0714-11ef-8e0e-94b86de0e66a','witness','SUfaU','2019-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('c8add1c3-0714-11ef-8e0e-94b86de0e66a','witness 2','valie','2013-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('c8adddc6-0714-11ef-8e0e-94b86de0e66a','priest','VALUd','1976-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('ceeca21c-0727-11ef-9a90-2f2838a388bf','lakipata','omosta','1934-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('cef85630-0727-11ef-9a90-2f2838a388bf','valimolit','olamina','1964-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('cef85aff-0727-11ef-9a90-2f2838a388bf','omarival','kaptivi','2003-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('cef85e4b-0727-11ef-9a90-2f2838a388bf','kaplatm','odowari','2003-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('d82e4760-d8be-11ee-8d30-dd530a390159','valen bona','kiproteach','2004-05-02','N','MALE',NULL),('d82e5312-d8be-11ee-8d30-dd530a390159','valuesvas','kiptoo','2024-05-02','N','MALE',NULL),('d82e571b-d8be-11ee-8d30-dd530a390159','mostal','usasalS','2020-03-02','N','MALE',NULL),('d82e5c0c-d8be-11ee-8d30-dd530a390159','janete','kilapan','2002-03-02','N','FEMALE',NULL),('e5f659f8-d8be-11ee-8d30-dd530a390159','valen bona','kiproteach','2004-05-02','N','MALE',NULL),('e5f66749-d8be-11ee-8d30-dd530a390159','valuesvas','kiptoo','2024-05-02','N','MALE',NULL),('e5f67198-d8be-11ee-8d30-dd530a390159','mostal','usasalS','2020-03-02','N','MALE',NULL),('e5f67a43-d8be-11ee-8d30-dd530a390159','janete','kilapan','2002-03-02','N','FEMALE',NULL),('e75fb89e-0727-11ef-9a90-2f2838a388bf','lakipata','omosta','1934-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a'),('e75fc73b-0727-11ef-9a90-2f2838a388bf','valimolit','olamina','1964-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('e75fcb3e-0727-11ef-9a90-2f2838a388bf','omarival','kaptivi','2003-01-23','N','MALE','71348d02-024d-11ef-921e-94b86de0e66a'),('e75fcee7-0727-11ef-9a90-2f2838a388bf','kaplatm','odowari','2003-01-23','N','FEMALE','71348d02-024d-11ef-921e-94b86de0e66a');
/*!40000 ALTER TABLE `PERSONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TRIBE`
--

DROP TABLE IF EXISTS `TRIBE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TRIBE` (
  `TRIBE_ID` varchar(255) NOT NULL,
  `TRIBE_NAME` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`TRIBE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TRIBE`
--

LOCK TABLES `TRIBE` WRITE;
/*!40000 ALTER TABLE `TRIBE` DISABLE KEYS */;
INSERT INTO `TRIBE` VALUES ('91e4914f-d73b-11ee-8358-94b86de0e66a','kikuyu');
/*!40000 ALTER TABLE `TRIBE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marriage_contract`
--

DROP TABLE IF EXISTS `marriage_contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marriage_contract` (
  `CONTRANT_ID` varchar(255) NOT NULL,
  `MARRIAGE_ID` varchar(255) DEFAULT NULL,
  `BY_CATHOLIC` enum('YES','NO') DEFAULT NULL,
  `DATE_` date DEFAULT NULL,
  `LOCATION_ID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`CONTRANT_ID`),
  KEY `MARRIAGE_ID` (`MARRIAGE_ID`),
  KEY `LOCATION_ID` (`LOCATION_ID`),
  CONSTRAINT `marriage_contract_ibfk_1` FOREIGN KEY (`MARRIAGE_ID`) REFERENCES `MARRIAGE_` (`MARRIAGE_ID`),
  CONSTRAINT `marriage_contract_ibfk_2` FOREIGN KEY (`LOCATION_ID`) REFERENCES `LOCATION` (`LOCATION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marriage_contract`
--

LOCK TABLES `marriage_contract` WRITE;
/*!40000 ALTER TABLE `marriage_contract` DISABLE KEYS */;
/*!40000 ALTER TABLE `marriage_contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'church_db'
--
/*!50003 DROP PROCEDURE IF EXISTS `batism` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `batism`()
BEGIN
	select b.BAPTISM_ID, concat(p3.FIRST_NAME ,' ', p3.LAST_NAME )  as god_child ,
	concat(p2.FIRST_NAME ,' ', p2.LAST_NAME )  as father,
 	concat(p.FIRST_NAME ,' ', p.LAST_NAME )  as mother,
 	g.G_FATHER_name,g.G_MOTHER_name
from BAPTISM b join
PERSONS p ON b.MOTHER_ID = p.PID
JOIN PERSONS p2 on b.FATHER_ID =p2.PID
join PERSONS p3 on b.G_CHILD = p3.PID
JOIN (
select gp.G_PERSONS_ID, gp.G_FATHER as G_FATHER_ID, 
CONCAT(p.FIRST_NAME ," ",p.LAST_NAME) as G_FATHER_name,
gp.G_MOTHER  as G_MOTHER_ID,
CONCAT(p2.FIRST_NAME ," ",p2.LAST_NAME) as G_MOTHER_name 
from G_PERSONS gp 
join PERSONS p  on gp.G_FATHER = p.PID  
join PERSONS p2  on gp.G_MOTHER  = p2.PID
) AS  g  ON  g.G_PERSONs_ID = b.g_PERSONS_ID ;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `edit_clan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `edit_clan`(
   cid varchar(255),
   tribe_id  varchar(255),
   clan_name  varchar(50)
)
begin
    update CLAN set TRIBE_ID=tribe_id,CLAN_NAME=clan_name 
    where  CID = cid;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `edit_death` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `edit_death`(
    death_id varchar(255),death_no int,pid varchar(255),so_or_do varchar(50),
    district_id varchar(255),baptism_id varchar(255),marriage_id varchar(255),
    last_rite enum('yes','no'), b_place varchar(255),b_date date,priest_id varchar(255)
)
begin
    update DEATHS set  DEATH_NO = death_no , PID = pid , SO_OR_DO = so_or_do , DISTRICT_ID = district_id , 
    BAPTISM_ID = baptism_id , MARRIAGE_ID = marriage_id , last_rite = l_rite , BURIAL_PLACE = b_place , BURIAL_DATE = b_date , 
    priest_id = p_id  where DEATH_ID  =  death_id ;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `edit_person` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `edit_person`(  
  pid varchar(255) ,
  first_name varchar(50),
  last_name varchar(50),
  date_of_birth date,
  gender enum('male','female'),
  clan_id varchar(255)
)
begin
    update PERSONS set FIRST_NAME=first_name,LAST_NAME=last_name,DATE_OF_BIRTH=date_of_birth,GENDER=gender,CLAN_ID=clan_id
    where  PID = pid;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `edit_tribe` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `edit_tribe`(
   tribe_id  varchar(255),
   tribe_name  varchar(50)
)
begin
    update TRIBE set tribe_NAME=tribe_name 
    where  TRIBE_ID= tribe_id;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_batism` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_batism`(
    baptism_no int, godchild json ,mother json,
    father json,baptism_at varchar(255), god_parent json)
begin
    declare god_father , god_mother json;
    declare godchild_id , mother_id ,father_id  varchar(255);
    declare g_persons_id, god_father_id ,god_mother_id varchar(255);

    declare exit handler for sqlexception
    begin
        rollback;
        resignal;
    end;
    start transaction;
    
    if godchild is not null then 
        set godchild_id = uuid();
       call json_insert_person(godchild_id,godchild);
       
    end if;

    
    if mother is not null then
        set mother_id = uuid();
       call json_insert_person(mother_id ,mother);
      
    end if;
    
    if father is not null then 
        set father_id = uuid();
       call json_insert_person(father_id ,father);
       
    end if;
    
    if god_parent is not null then 

    
        set god_father = json_extract(god_parent,'$.god_father');
        set god_father_id= uuid();
       call json_insert_person(god_father_id ,god_father);
      
    
        set god_mother_id= uuid();
        set god_mother =json_extract(god_parent,'$.god_mother');
       call json_insert_person(god_mother_id ,god_mother);
     
     	set g_persons_id = uuid();
        insert into G_PERSONS(G_PERSONS_ID,G_FATHER,S_O_father,G_MOTHER,S_O_mother)
        values(g_persons_id,god_father_id,
	        json_unquote(json_extract(god_parent,'$.s_o_father')),
            god_mother_id,
	        json_unquote(json_extract(god_parent,'$.s_o_mother'))
        );
    end if;
    
   
    insert into BAPTISM (BAPTISM_ID ,BAPTISM_NO ,G_CHILD,MOTHER_ID ,FATHER_ID ,BAPTISM_AT , g_PERSONS_ID )
    values(uuid() , baptism_no , godchild_id , mother_id , father_id , baptism_at , g_persons_id);
    commit;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_clan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_clan`(  
   tribe_id  varchar(255),
   clan_name  varchar(50)
)
begin
    insert into CLAN (CID,TRIBE_ID,CLAN_NAME)
    values(uuid(),tribe_id,clan_name);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_couple` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_couple`(
  marriage_id varchar(255),
  bride json,
  mother  json,
  father json
)
begin

    declare exit handler for sqlexception
    begin
        rollback;
        resignal;
    end;
    start transaction;
    
    if bride is not null then 
      call  json_insert_person(uuid(),godchild);
    end if;

    
    if mother is not null then
      call  json_insert_person(uuid(),mother);
    end if;
    
    if father is not null then 
       call json_insert_person(uuid(),father);
    end if;
    
    insert into BAPTISM (BAPTISM_ID ,BAPTISM_NO ,MOTHER_ID ,FATHER_ID ,BAPTISM_AT , g_PERSONS_ID )
    values(uuid() , baptism_no , godchild_id , mother_id , father_id , baptism_at , g_persons_id);
    commit;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_death` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_death`(
    death_no int,pid varchar(255),so_or_do varchar(50),
    district_id varchar(255),baptism_id varchar(255),marriage_id varchar(255),
    last_rite enum('yes','no'), burial_place varchar(255),burial_date date,priest_id varchar(255)
)
begin
    insert into DEATHS (DEATH_ID,DEATH_NO,PID,SO_OR_DO,DISTRICT_ID,BAPTISM_ID,MARRIAGE_ID,last_rite,BURIAL_PLACE,BURIAL_DATE,priest_id ) 
    values( uuid(),death_no,pid,so_or_do,district_id,baptism_id,marriage_id,last_rite,burial_place,burial_date,priest_id );
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_marriage` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_marriage`(
    date_ date, church_of varchar(50),banns_no int,
    delegate json,priest json,male_witness json,
    female_witness json,m_cert_no int
)
begin

	declare delegate_id ,priest_id, male_witness_id ,female_witness_id varchar(255);

    declare exit  handler for sqlexception
    begin
        rollback;
        resignal;
    end;
    start transaction;
   
    if delegate is not null then 
        set delegate_id = uuid();
       
       	call  json_insert_person(delegate_id,delegate);
       	
    end if;
   
    if priest is not null then 
        set priest_id = uuid();
       
       	call  json_insert_person(priest_id,priest);
     
    end if;
    
    if male_witness is not null then 
        set male_witness_id = uuid();
      	call  json_insert_person(male_witness_id,male_witness);
     	
    end if;
    
    if female_witness is not null then 
        set female_witness_id = uuid();
      	call  json_insert_person(female_witness_id,female_witness);
     
    end if;
    insert into MARRIAGE_(MARRIAGE_ID ,DATE_ , CHURCH_OF ,BANNS_NO ,DELEGATE_ ,PRIEST_ID ,MALE_WITNESS_ID ,FEMALE_WITNESS_ID ,M_CERT_NO )
    values(uuid(),date_ ,church_of,banns_no ,delegate_id,priest_id ,male_witness_id ,female_witness_id, m_cert_no );
    commit;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_tribe` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_tribe`(  
   tribe_name varchar(50)
)
begin
    insert into TRIBE (TRIBE_ID, TRIBE_NAME)
    values(uuid(),tribe_name);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `json_insert_person` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `json_insert_person`( in person_id varchar(255),in person json )
begin

    if person is not null then
        insert into PERSONS (PID,FIRST_NAME,LAST_NAME,DATE_OF_BIRTH,GENDER,CLAN_ID) 
        values( person_id,
            json_unquote(json_extract(person,'$.FIRST_NAME')),
	        json_unquote(json_extract(person,'$.LAST_NAME')),
	        json_unquote(json_extract(person,'$.DATE_OF_BIRTH')),
	        json_unquote(json_extract(person,'$.GENDER')),
	        json_unquote(json_extract(person,'$.CLAN_ID'))
        );
        /*select "insert data";*/
    end if;
    /*select "you have";*/
    
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `select_clan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `select_clan`(
   cid varchar(255),
   tribe_id  varchar(255)
)
begin
    if cid and tribe_id is null then
        select C.CID, T.TRIBE_NAME, C.CLAN_NAME
        from CLAN as C 
        join TRIBE  as T  on C.TRIBE_ID = T.TRIBE_ID;

    elseif cid  is null then
        select C.CID, T.TRIBE_NAME, C.CLAN_NAME
        from CLAN as C  
        join TRIBE  as T  on C.TRIBE_ID = T.TRIBE_ID 
        where T.TRIBE_ID = tribe_id;

    elseif tribe_id is null then 
        select C.CID, T.TRIBE_NAME, C.CLAN_NAME
        from CLAN as C  
        join TRIBE  as T  on C.TRIBE_ID = T.TRIBE_ID 
        where C.CID = cid;

    else
        select C.CID, T.TRIBE_NAME, C.CLAN_NAME
        from CLAN as C 
        join TRIBE  as T  on C.TRIBE_ID = T.TRIBE_ID 
        where C.CID = cid and T.TRIBE_ID = tribe_id;
    end if;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `_death` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `_death`(death_no int ,death_id varchar(255))
begin
    if death_no or death_id is null then

        select D.DEATH_NO , concat(P.FIRST_NAME, " ",P.LAST_NAME) as person_name , dis.LOC_NAME , 
        B.BAPTISM_NO,M.M_CERT_NO ,D.last_rite , L.LOC_NAME, D.BURIAL_DATE ,concat(v.FIRST_NAME, " ",v.LAST_NAME) as priest_name 
        from DEATHS  as D
        join (select PID ,FIRST_NAME , LAST_NAME  from  PERSONS  ) as P on D.PID = P.PID
        join BAPTISM as B on D.BAPTISM_ID = B.BAPTISM_ID
        join MARRIAGE_ as M  on D.MARRIAGE_ID = M.MARRIAGE_ID
        join LOCATION as L on D.BURIAL_PLACE = L.LOCATION_ID
        join (select PID ,FIRST_NAME , LAST_NAME  from  PERSONS ) as V on D.PID = V.PID
        where  D.DEATH_NO = death_no or DEATH_ID = death_id;
    else
        select D.DEATH_NO , concat(P.FIRST_NAME, " ",P.LAST_NAME) as person_name  
        from DEATHS  as D
        join (select PID ,FIRST_NAME , LAST_NAME  from  PERSONS  ) as P on D.PID = P.PID;
    end if;

end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-01 14:18:51
