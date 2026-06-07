CREATE DATABASE  IF NOT EXISTS `library_collection` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `library_collection`;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: library_collection
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accessrequest`
--

DROP TABLE IF EXISTS `accessrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accessrequest` (
  `requestID` int NOT NULL AUTO_INCREMENT,
  `itemID` int DEFAULT NULL,
  `memberID` int DEFAULT NULL,
  `requestReason` varchar(100) NOT NULL,
  `requestStatus` varchar(30) NOT NULL,
  `requestTimestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`requestID`),
  KEY `itemID` (`itemID`),
  KEY `memberID` (`memberID`),
  CONSTRAINT `accessrequest_ibfk_1` FOREIGN KEY (`itemID`) REFERENCES `collectionitem` (`itemID`),
  CONSTRAINT `accessrequest_ibfk_2` FOREIGN KEY (`memberID`) REFERENCES `librarymember` (`MemberID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accessrequest`
--

LOCK TABLES `accessrequest` WRITE;
/*!40000 ALTER TABLE `accessrequest` DISABLE KEYS */;
/*!40000 ALTER TABLE `accessrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accessreview`
--

DROP TABLE IF EXISTS `accessreview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accessreview` (
  `reviewID` int NOT NULL AUTO_INCREMENT,
  `itemID` int DEFAULT NULL,
  `ElderID` int DEFAULT NULL,
  `reviewNotes` varchar(200) DEFAULT NULL,
  `accessOutcome` varchar(30) DEFAULT NULL,
  `reviewTimestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`reviewID`),
  KEY `itemID` (`itemID`),
  KEY `ElderID` (`ElderID`),
  CONSTRAINT `accessreview_ibfk_1` FOREIGN KEY (`itemID`) REFERENCES `collectionitem` (`itemID`),
  CONSTRAINT `accessreview_ibfk_2` FOREIGN KEY (`ElderID`) REFERENCES `communityelder` (`ElderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accessreview`
--

LOCK TABLES `accessreview` WRITE;
/*!40000 ALTER TABLE `accessreview` DISABLE KEYS */;
/*!40000 ALTER TABLE `accessreview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collectionitem`
--

DROP TABLE IF EXISTS `collectionitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collectionitem` (
  `itemID` int NOT NULL AUTO_INCREMENT,
  `employeeID` int DEFAULT NULL,
  `title` varchar(50) NOT NULL,
  `description` varchar(300) NOT NULL,
  `imageLink` varchar(30) DEFAULT NULL,
  `itemType` varchar(30) NOT NULL,
  `itemCategory` varchar(30) NOT NULL,
  `reviewStatus` varchar(20) DEFAULT NULL,
  `accessStatus` varchar(25) NOT NULL,
  `accessConsideration` varchar(100) DEFAULT NULL,
  `sensitivityLevel` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`itemID`),
  KEY `employeeID` (`employeeID`),
  CONSTRAINT `collectionitem_ibfk_1` FOREIGN KEY (`employeeID`) REFERENCES `librarystaff` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collectionitem`
--

LOCK TABLES `collectionitem` WRITE;
/*!40000 ALTER TABLE `collectionitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `collectionitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `communityelder`
--

DROP TABLE IF EXISTS `communityelder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communityelder` (
  `ElderID` int NOT NULL AUTO_INCREMENT,
  `CommunityName` varchar(50) DEFAULT NULL,
  `id` int DEFAULT NULL,
  PRIMARY KEY (`ElderID`),
  KEY `id` (`id`),
  CONSTRAINT `communityelder_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communityelder`
--

LOCK TABLES `communityelder` WRITE;
/*!40000 ALTER TABLE `communityelder` DISABLE KEYS */;
INSERT INTO `communityelder` VALUES (1,'Dharug Country',3),(2,'Yuggera Country',5);
/*!40000 ALTER TABLE `communityelder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librarymember`
--

DROP TABLE IF EXISTS `librarymember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarymember` (
  `MemberID` int NOT NULL AUTO_INCREMENT,
  `id` int DEFAULT NULL,
  PRIMARY KEY (`MemberID`),
  KEY `id` (`id`),
  CONSTRAINT `librarymember_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarymember`
--

LOCK TABLES `librarymember` WRITE;
/*!40000 ALTER TABLE `librarymember` DISABLE KEYS */;
INSERT INTO `librarymember` VALUES (1,1),(2,6);
/*!40000 ALTER TABLE `librarymember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librarystaff`
--

DROP TABLE IF EXISTS `librarystaff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarystaff` (
  `EmployeeID` int NOT NULL AUTO_INCREMENT,
  `PositionTitle` varchar(50) DEFAULT NULL,
  `ID` int DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  KEY `ID` (`ID`),
  CONSTRAINT `librarystaff_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarystaff`
--

LOCK TABLES `librarystaff` WRITE;
/*!40000 ALTER TABLE `librarystaff` DISABLE KEYS */;
INSERT INTO `librarystaff` VALUES (1,'Curator',2,'2026-01-02'),(2,'Admin',4,'2025-06-04');
/*!40000 ALTER TABLE `librarystaff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fullName` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Ben Smith','bensmith@gmail.com','0456998299','password123'),(2,'Natalie Moore','nmoore@library.com','0433899766','red.apples4'),(3,'Bethany Gardiner','bethgard@gmail.com','0433876987','oranges44'),(4,'Chloe Kennedy','ckennedy@library.com','0477209892','123456789'),(5,'Scott Black','scotty@gmail.com','0400387776','pa$$w0rd'),(6,'Betty Smith','betty@hotmail.com','0404988325','roses33');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-08  6:30:17
