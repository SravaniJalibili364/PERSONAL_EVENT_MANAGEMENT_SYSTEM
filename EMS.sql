-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: EMS
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

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
-- Table structure for table `event_table`
--

DROP TABLE IF EXISTS `event_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_table` (
  `user_name` varchar(30) NOT NULL,
  `event_id` int NOT NULL,
  `event_name` varchar(100) NOT NULL,
  `event_type` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `date` timestamp NOT NULL,
  `Gift` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_table`
--

LOCK TABLES `event_table` WRITE;
/*!40000 ALTER TABLE `event_table` DISABLE KEYS */;
INSERT INTO `event_table` VALUES ('prasanna',1,'reception','marriage','thirupathi','2021-10-11 00:00:00','Dinner set'),('rukhiya',2,'bharath','marriage','prakasam','2021-10-11 02:00:00','ring'),('sowmya',3,'mehandhi','marriage','srikakulam','2021-10-17 02:00:00','flower bouquet'),('bhavani',4,'birthday-bash','Birthday','bhimavaram','2021-10-13 12:00:00','Watch'),('vasanthi',5,'1st anniversary','Anniversary','guntur','2021-10-14 08:00:00','Jewerelly'),('ramya',6,'2nd  anniversary','Anniversary','krishna','2021-10-16 09:00:00','Necklace'),('likki',7,'silver Jubliee','marriage','krishna','2021-10-18 10:00:00','Bangles'),('yamini',8,'diomond jubliee','marriage','kurnool','2021-10-10 11:00:00','flower bouquet'),('satya',9,'Engangement','marriage','kadapa','2021-10-09 07:00:00','Engangement ring'),('Teju',123,'Spinster Party','Bachelours Party','Vizag','2021-10-10 06:40:20',NULL),('Sameera',410,'10th Anniversary','Anniversary','vizag','2021-10-11 22:22:21','Flowers'),('kaki',541,'cygnus','college fest','nuzvid','2021-10-15 06:42:12',NULL),(' Divya',780,'marriage','marriage','vizag','2021-10-01 18:30:00',NULL),('Sirisha',888,'vacation','trip','vizag','2021-10-11 23:22:12','Home Appliances'),('Sravani Jalibili',150364,'Birthday','Birthday_function','vijayawada','2021-10-01 18:30:00',NULL);
/*!40000 ALTER TABLE `event_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-09 10:04:11
