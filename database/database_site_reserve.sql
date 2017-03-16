-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: database
-- ------------------------------------------------------
-- Server version	5.6.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `site_reserve`
--

DROP TABLE IF EXISTS `site_reserve`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `site_reserve` (
  `siteid` varchar(10) NOT NULL,
  `sitetype` varchar(20) NOT NULL,
  `userid` varchar(10) NOT NULL,
  `time_sta` varchar(45) NOT NULL,
  `time_end` varchar(45) NOT NULL,
  `code` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`siteid`,`time_end`,`time_sta`,`userid`,`sitetype`),
  KEY `reserveid_idx` (`userid`),
  KEY `siteid_idx` (`siteid`,`sitetype`),
  CONSTRAINT `reserveid` FOREIGN KEY (`userid`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `siteid` FOREIGN KEY (`siteid`, `sitetype`) REFERENCES `site` (`id`, `type`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `site_reserve`
--

LOCK TABLES `site_reserve` WRITE;
/*!40000 ALTER TABLE `site_reserve` DISABLE KEYS */;
INSERT INTO `site_reserve` VALUES ('1','篮球场','14061064','2016-11-12 02:00:00','2016-11-12 03:00:00','2221'),('1','篮球场','14061064','2016-11-12 04:00:00','2016-11-12 05:00:00','8700');
/*!40000 ALTER TABLE `site_reserve` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-25 17:00:58
