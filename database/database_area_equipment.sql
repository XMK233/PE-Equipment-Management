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
-- Table structure for table `area_equipment`
--

DROP TABLE IF EXISTS `area_equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `area_equipment` (
  `equipid` varchar(10) NOT NULL,
  `areaid` varchar(10) NOT NULL,
  `qty` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`equipid`,`areaid`),
  KEY `qty_area_idx` (`areaid`),
  CONSTRAINT `qty_area` FOREIGN KEY (`areaid`) REFERENCES `area` (`areaid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `qty_equip` FOREIGN KEY (`equipid`) REFERENCES `equipment` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area_equipment`
--

LOCK TABLES `area_equipment` WRITE;
/*!40000 ALTER TABLE `area_equipment` DISABLE KEYS */;
INSERT INTO `area_equipment` VALUES ('E1','A1','47'),('E1','A2','50'),('E10','A1','4'),('E2','A1','50'),('E2','A2','50'),('E3','A1','50'),('E3','A2','50'),('E4','A1','50'),('E4','A2','50'),('E5','A1','50'),('E5','A2','50'),('E6','A1','50'),('E7','A1','50'),('E8','A1','50'),('E9','A1','8');
/*!40000 ALTER TABLE `area_equipment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-25 17:01:08
