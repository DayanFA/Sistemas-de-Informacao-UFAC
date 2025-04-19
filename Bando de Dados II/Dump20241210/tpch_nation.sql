CREATE DATABASE  IF NOT EXISTS `tpch` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tpch`;
-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: tpch
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

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
-- Table structure for table `nation`
--

DROP TABLE IF EXISTS `nation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nation` (
  `n_nationkey` decimal(10,0) DEFAULT NULL,
  `n_name` char(25) DEFAULT NULL,
  `n_regionkey` decimal(10,0) DEFAULT NULL,
  `n_comment` varchar(152) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nation`
--

LOCK TABLES `nation` WRITE;
/*!40000 ALTER TABLE `nation` DISABLE KEYS */;
INSERT INTO `nation` VALUES (0,'ALGERIA',0,'haggle. carefully final deposits detect slyly agai'),(1,'ARGENTINA',1,'al foxes promise slyly according to the regular accounts. bold requests alon'),(2,'BRAZIL',1,'y alongside of the pending deposits. carefully special packages are about the ironic forges. slyly special'),(3,'CANADA',1,'eas hang ironic, silent packages. slyly regular packages are furiously over the tithes. fluffily bold'),(4,'EGYPT',4,'y above the carefully unusual theodolites. final dugouts are quickly across the furiously regular d'),(5,'ETHIOPIA',0,'ven packages wake quickly. regu'),(6,'FRANCE',3,'refully final requests. regular, ironi'),(7,'GERMANY',3,'l platelets. regular accounts x-ray: unusual, regular acco'),(8,'INDIA',2,'ss excuses cajole slyly across the packages. deposits print aroun'),(9,'INDONESIA',2,'slyly express asymptotes. regular deposits haggle slyly. carefully ironic hockey players sleep blithely. carefull'),(10,'IRAN',4,'efully alongside of the slyly final dependencies. '),(11,'IRAQ',4,'nic deposits boost atop the quickly final requests? quickly regula'),(12,'JAPAN',2,'ously. final, express gifts cajole a'),(13,'JORDAN',4,'ic deposits are blithely about the carefully regular pa'),(14,'KENYA',0,'pending excuses haggle furiously deposits. pending, express pinto beans wake fluffily past t'),(15,'MOROCCO',0,'rns. blithely bold courts among the closely regular packages use furiously bold platelets?'),(16,'MOZAMBIQUE',0,'s. ironic, unusual asymptotes wake blithely r'),(17,'PERU',1,'platelets. blithely pending dependencies use fluffily across the even pinto beans. carefully silent accoun'),(18,'CHINA',2,'c dependencies. furiously express notornis sleep slyly regular accounts. ideas sleep. depos'),(19,'ROMANIA',3,'ular asymptotes are about the furious multipliers. express dependencies nag above the ironically ironic account'),(20,'SAUDI ARABIA',4,'ts. silent requests haggle. closely express packages sleep across the blithely'),(21,'VIETNAM',2,'hely enticingly express accounts. even, final '),(22,'RUSSIA',3,'requests against the platelets use never according to the quickly regular pint'),(23,'UNITED KINGDOM',3,'eans boost carefully special requests. accounts are. carefull'),(24,'UNITED STATES',1,'y final packages. slow foxes cajole quickly. quickly silent platelets breach ironic accounts. unusual pinto be');
/*!40000 ALTER TABLE `nation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-10 11:55:11
