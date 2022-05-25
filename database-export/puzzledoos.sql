CREATE DATABASE  IF NOT EXISTS `puzzlebox` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `puzzlebox`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: puzzlebox
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `acties`
--

DROP TABLE IF EXISTS `acties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acties` (
  `actieID` int NOT NULL,
  `Actiebeschrijving` varchar(300) NOT NULL,
  PRIMARY KEY (`actieID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acties`
--

LOCK TABLES `acties` WRITE;
/*!40000 ALTER TABLE `acties` DISABLE KEYS */;
INSERT INTO `acties` VALUES (1,'Donec feugiat metus sit amet ante. Vivamus non'),(2,'feugiat non, lobortis quis, pede. Suspendisse dui. Fusce'),(3,'libero. Proin sed turpis nec mauris blandit mattis.'),(4,'nonummy ac, feugiat non, lobortis quis, pede. Suspendisse'),(5,'Donec luctus aliquet odio. Etiam ligula tortor, dictum'),(6,'Sed nunc est, mollis non, cursus non, egestas'),(7,'tincidunt aliquam arcu. Aliquam ultrices iaculis odio. Nam'),(8,'gravida. Praesent eu nulla at sem molestie sodales.'),(9,'imperdiet ullamcorper. Duis at lacus. Quisque purus sapien,'),(10,'eu odio tristique pharetra. Quisque ac libero nec'),(11,'ullamcorper eu, euismod ac, fermentum vel, mauris. Integer'),(12,'cursus non, egestas a, dui. Cras pellentesque. Sed'),(13,'gravida nunc sed pede. Cum sociis natoque penatibus'),(14,'Aenean euismod mauris eu elit. Nulla facilisi. Sed'),(15,'ut odio vel est tempor bibendum. Donec felis'),(16,'metus eu erat semper rutrum. Fusce dolor quam,'),(17,'sed, hendrerit a, arcu. Sed et libero. Proin'),(18,'cursus et, magna. Praesent interdum ligula eu enim.'),(19,'nulla vulputate dui, nec tempus mauris erat eget'),(20,'sed tortor. Integer aliquam adipiscing lacus. Ut nec'),(21,'Nulla eget metus eu erat semper rutrum. Fusce'),(22,'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'),(23,'ac facilisis facilisis, magna tellus faucibus leo, in'),(24,'sagittis semper. Nam tempor diam dictum sapien. Aenean'),(25,'dictum eleifend, nunc risus varius orci, in consequat'),(26,'eu tellus. Phasellus elit pede, malesuada vel, venenatis'),(27,'neque. Morbi quis urna. Nunc quis arcu vel'),(28,'euismod mauris eu elit. Nulla facilisi. Sed neque.'),(29,'hendrerit id, ante. Nunc mauris sapien, cursus in,'),(30,'facilisi. Sed neque. Sed eget lacus. Mauris non'),(31,'Vestibulum accumsan neque et nunc. Quisque ornare tortor'),(32,'elit sed consequat auctor, nunc nulla vulputate dui,'),(33,'dignissim. Maecenas ornare egestas ligula. Nullam feugiat placerat'),(34,'metus. Aliquam erat volutpat. Nulla facilisis. Suspendisse commodo'),(35,'vel turpis. Aliquam adipiscing lobortis risus. In mi'),(36,'sit amet luctus vulputate, nisi sem semper erat,'),(37,'diam. Pellentesque habitant morbi tristique senectus et netus'),(38,'nec, eleifend non, dapibus rutrum, justo. Praesent luctus.'),(39,'dictum placerat, augue. Sed molestie. Sed id risus'),(40,'sed, hendrerit a, arcu. Sed et libero. Proin'),(41,'sed dui. Fusce aliquam, enim nec tempus scelerisque,'),(42,'Mauris ut quam vel sapien imperdiet ornare. In'),(43,'magna. Praesent interdum ligula eu enim. Etiam imperdiet'),(44,'et ultrices posuere cubilia Curae Phasellus ornare. Fusce'),(45,'convallis, ante lectus convallis est, vitae sodales nisi'),(46,'nascetur ridiculus mus. Proin vel nisl. Quisque fringilla'),(47,'Pellentesque tincidunt tempus risus. Donec egestas. Duis ac'),(48,'ligula tortor, dictum eu, placerat eget, venenatis a,'),(49,'ut, nulla. Cras eu tellus eu augue porttitor'),(50,'Praesent eu dui. Cum sociis natoque penatibus et'),(51,'leo. Vivamus nibh dolor, nonummy ac, feugiat non,'),(52,'posuere at, velit. Cras lorem lorem, luctus ut,');
/*!40000 ALTER TABLE `acties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device` (
  `DeviceID` int NOT NULL,
  `Naam` varchar(200) NOT NULL,
  `Merk` varchar(200) NOT NULL,
  `Beschrijving` varchar(300) NOT NULL,
  `Type` varchar(100) NOT NULL,
  `Aankoopkost` int NOT NULL,
  `Meeteenheid` varchar(45) NOT NULL,
  PRIMARY KEY (`DeviceID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` VALUES (1,'pharetra','In Lobortis PC','nibh lacinia orci, consectetuer','lorem.',17,'lorem'),(2,'Phasellus','Lobortis Class LLC','convallis convallis dolor. Quisque tincidunt pede','a',79,'orci,'),(3,'ligula.','Lorem Sit Associates','Phasellus vitae mauris sit amet lorem','Quisque',9,'iaculis'),(4,'lectus.','Adipiscing Non Consulting','dui, in sodales elit erat vitae risus. Duis a','gravida.',46,'Phasellus'),(5,'auctor','Nam Consulting','neque. Nullam ut nisi','a',42,'Suspendisse'),(6,'eu','Nulla Facilisi Sed Foundation','mollis nec,','Aenean',99,'placerat.'),(7,'ornare','Vitae Dolor Limited','auctor, velit eget laoreet posuere, enim','Aenean',0,'mauris'),(8,'risus','Amet LLP','Aliquam adipiscing lobortis risus. In mi','Aenean',30,'diam.'),(9,'dapibus','Augue LLP','turpis nec mauris blandit mattis. Cras eget nisi','fringilla',10,'Nunc'),(10,'nulla','Cubilia Curae Foundation','mollis. Phasellus libero','molestie',87,'sapien,'),(11,'non','Rhoncus Proin Corp.','blandit. Nam nulla magna, malesuada vel, convallis in, cursus','et',55,'dolor'),(12,'non','Porta Elit Limited','euismod est arcu ac orci.','quis',92,'ultricies'),(13,'at','Ullamcorper Nisl Corp.','auctor, velit eget laoreet posuere','enim',99,'auctor'),(14,'nunc','Arcu Curabitur Ut Associates','at, nisi. Cum sociis natoque','dolor.',2,'Cras'),(15,'Duis','Vivamus Rhoncus Company','varius orci, in consequat enim diam vel arcu.','at,',92,'ad'),(16,'tempor','Non Foundation','malesuada','fermentum',42,'enim'),(17,'risus.','Convallis Est Vitae Ltd','sit amet lorem semper auctor. Mauris vel turpis. Aliquam','Donec',77,'Proin'),(18,'nec','Cum Sociis Industries','congue turpis. In condimentum. Donec at arcu. Vestibulum ante','dui',88,'dis'),(19,'Vestibulum','Ridiculus Consulting','magnis dis parturient montes, nascetur ridiculus mus. Donec dignissim','montes,',49,'interdum.'),(20,'pretium','Adipiscing Incorporated','accumsan neque et nunc. Quisque ornare tortor','ligula',62,'ante'),(21,'et','Parturient Montes LLP','luctus et ultrices posuere','ante',83,'Sed'),(22,'ac','Faucibus Corporation','montes, nascetur ridiculus mus. Proin','vel',75,'elit.'),(23,'justo','Tristique Senectus LLC','nec, malesuada ut, sem. Nulla interdum. Curabitur','fames',46,'tempor'),(24,'mauris','Luctus Curabitur Corporation','vel, convallis','sit',64,'massa'),(25,'mauris.','Nam Tempor Foundation','arcu. Vestibulum ante ipsum primis in','arcu.',26,'Etiam'),(26,'non','A Enim Foundation','parturient montes, nascetur ridiculus mus. Proin vel arcu eu','turpis',88,'nisi'),(27,'ante','At Velit Industries','ipsum. Phasellus vitae mauris sit amet','turpis',79,'semper'),(28,'eu','Magna Phasellus PC','orci, in consequat','dis',32,'ultrices,'),(29,'enim.','Sapien Cursus Ltd','sapien. Cras dolor dolor, tempus non, lacinia at,','pretium',92,'convallis'),(30,'Donec','Morbi Quis Urna Corp.','natoque penatibus et magnis dis parturient','augue',59,'convallis'),(31,'vel','Tellus Imperdiet Corp.','luctus lobortis. Class aptent','Suspendisse',87,'ac'),(32,'dictum','Dictum LLP','penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean','facilisi.',48,'enim,'),(33,'Morbi','Tristique Senectus Foundation','elit, dictum eu, eleifend nec, malesuada ut, sem.','Vivamus',25,'enim'),(34,'sed','Auctor Non Feugiat Incorporated','Praesent interdum ligula eu enim. Etiam imperdiet','neque',43,'Curabitur'),(35,'odio.','Volutpat Ornare Incorporated','feugiat metus sit amet','Sed',63,'tellus'),(36,'Nunc','Odio Nam Inc.','ut erat. Sed nunc','orci',27,'vulputate'),(37,'dolor','Non Egestas LLC','Donec est mauris, rhoncus id, mollis nec, cursus','dui.',79,'velit.'),(38,'magnis','Odio Semper Company','risus a ultricies adipiscing, enim mi tempor','non',45,'sed'),(39,'tincidunt','Libero Dui Industries','id, blandit at,','commodo',32,'feugiat'),(40,'In','Erat Semper Ltd','non enim. Mauris quis turpis vitae','hendrerit.',77,'sagittis'),(41,'euismod','Laoreet Lectus Limited','et magnis dis parturient montes, nascetur ridiculus mus. Proin vel','ultrices.',52,'ut,'),(42,'quam.','Non LLC','Fusce mollis. Duis sit amet diam','in',86,'mollis'),(43,'ipsum.','Tristique Ac Eleifend Institute','lobortis. Class aptent taciti sociosqu','elementum',28,'in'),(44,'nec','Est Ac Inc.','at sem molestie sodales. Mauris blandit enim consequat purus.','non',55,'semper'),(45,'magna','Enim Condimentum Limited','dolor','eleifend.',79,'ligula'),(46,'eu','Odio Corporation','ligula. Nullam feugiat placerat velit. Quisque varius. Nam','metus',88,'nibh'),(47,'metus','Libero Et Corporation','lacus. Mauris non dui nec urna suscipit','natoque',70,'mattis'),(48,'cursus','Est Ac Foundation','libero est, congue a, aliquet vel,','nisl',88,'amet'),(49,'Quisque','Cursus Luctus Incorporated','Nunc ac sem ut dolor dapibus','a',91,'libero'),(50,'habitant','Adipiscing Elit Incorporated','in consectetuer ipsum nunc id enim.','Aliquam',24,'at,');
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historiek`
--

DROP TABLE IF EXISTS `historiek`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historiek` (
  `Volgnummer` int NOT NULL,
  `Actiedatum` datetime NOT NULL,
  `Waarde` varchar(45) NOT NULL,
  `Commentaar` varchar(300) NOT NULL,
  `DeviceID` int NOT NULL,
  `ActieID` int NOT NULL,
  `SpelerID` int NOT NULL,
  `VraagID` int NOT NULL,
  PRIMARY KEY (`Volgnummer`),
  KEY `Deviceid_idx` (`DeviceID`),
  KEY `Actieid_idx` (`ActieID`),
  KEY `spelerID_idx` (`SpelerID`),
  KEY `vraagID_idx` (`VraagID`),
  CONSTRAINT `Actieid` FOREIGN KEY (`ActieID`) REFERENCES `acties` (`actieID`),
  CONSTRAINT `Deviceid` FOREIGN KEY (`DeviceID`) REFERENCES `device` (`DeviceID`),
  CONSTRAINT `spelerID` FOREIGN KEY (`SpelerID`) REFERENCES `spelers` (`SpelersID`),
  CONSTRAINT `vraagID` FOREIGN KEY (`VraagID`) REFERENCES `vragen` (`vragenID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historiek`
--

LOCK TABLES `historiek` WRITE;
/*!40000 ALTER TABLE `historiek` DISABLE KEYS */;
INSERT INTO `historiek` VALUES (1,'2022-06-05 03:36:00','526','in, tempus eu, ligula. Aenean',1,1,1,1),(2,'2022-10-21 22:44:00','272','Mauris ut',2,2,2,2),(3,'2022-10-10 14:53:00','943','lacus. Aliquam rutrum lorem ac risus. Morbi metus.',3,3,3,3),(4,'2022-01-14 23:15:00','567','neque vitae semper egestas, urna justo faucibus',4,4,4,4),(5,'2022-11-23 22:35:00','180','vel sapien imperdiet ornare. In',5,5,5,5),(6,'2023-05-03 16:44:00','418','dolor. Quisque tincidunt pede ac urna. Ut',6,6,6,6),(7,'2023-02-02 07:08:00','285','est, congue a, aliquet vel, vulputate',7,7,7,7),(8,'2022-07-29 05:46:00','245','libero at auctor ullamcorper,',8,8,8,8),(9,'2022-02-13 21:32:00','504','elit sed consequat auctor, nunc',9,9,9,9),(10,'2022-08-04 14:10:00','396','et risus. Quisque libero',10,10,10,10),(11,'2021-11-09 04:22:00','308','Quisque',11,11,11,11),(12,'2022-06-06 12:22:00','638','malesuada id, erat. Etiam vestibulum massa rutrum',12,12,12,12),(13,'2022-12-12 09:16:00','450','luctus et',13,13,13,13),(14,'2022-06-09 23:31:00','120','neque. Nullam ut nisi a odio semper',14,14,14,14),(15,'2022-11-22 08:23:00','71','odio. Phasellus at augue id ante dictum',15,15,15,15),(16,'2022-08-27 13:46:00','806','imperdiet non, vestibulum nec,',16,16,16,16),(17,'2023-01-07 22:40:00','770','Nullam enim. Sed nulla ante, iaculis',17,17,17,17),(18,'2022-08-05 03:01:00','823','purus ac tellus.',18,18,18,18),(19,'2022-02-17 09:13:00','597','tempus non, lacinia at, iaculis quis,',19,19,19,19),(20,'2023-01-18 04:48:00','531','consequat enim diam vel arcu. Curabitur ut odio',20,20,20,20),(21,'2021-09-03 21:09:00','298','magna. Lorem ipsum dolor sit amet,',21,21,21,21),(22,'2022-04-11 07:36:00','786','nibh. Phasellus nulla.',22,22,22,22),(23,'2022-12-23 00:21:00','409','libero. Morbi accumsan',23,23,23,23),(24,'2022-03-23 06:46:00','238','vitae',24,24,24,24),(25,'2021-12-14 22:05:00','562','interdum. Nunc sollicitudin commodo ipsum. Suspendisse non',25,25,25,25),(26,'2021-06-21 14:53:00','818','Donec tincidunt. Donec vitae erat',26,26,26,26),(27,'2022-01-17 00:40:00','824','ac turpis egestas.',27,27,27,27),(28,'2023-05-16 12:48:00','215','turpis.',28,28,28,28),(29,'2023-01-04 04:44:00','529','dictum mi, ac mattis',29,29,29,29),(30,'2022-10-17 17:53:00','931','eget metus. In',30,30,30,30),(31,'2022-03-05 17:21:00','274','adipiscing lacus. Ut nec',31,31,31,31),(32,'2022-04-05 05:08:00','728','lorem vitae odio',32,32,32,32),(33,'2022-11-13 03:17:00','500','nascetur ridiculus mus. Proin vel arcu',33,33,33,33),(34,'2023-02-03 15:27:00','682','ornare, elit elit',34,34,34,34),(35,'2021-07-15 19:06:00','551','sociis natoque',35,35,35,35),(36,'2022-03-08 07:50:00','654','penatibus et magnis dis parturient montes,',36,36,36,36),(37,'2021-08-04 09:17:00','192','velit dui,',37,37,37,37),(38,'2023-04-08 10:26:00','890','porttitor tellus non magna. Nam ligula elit,',38,38,38,38),(39,'2022-02-06 01:33:00','464','vitae risus. Duis a',39,39,39,39),(40,'2022-08-30 06:23:00','216','eget, ipsum. Donec sollicitudin adipiscing ligula.',40,40,40,40),(41,'2022-12-19 21:37:00','92','Cras convallis convallis dolor. Quisque',41,41,41,41),(42,'2022-08-29 23:56:00','45','Donec nibh. Quisque nonummy ipsum non arcu. Vivamus',42,42,42,42),(43,'2022-03-09 08:23:00','482','Etiam ligula tortor, dictum eu, placerat eget,',43,43,43,43),(44,'2022-05-18 03:35:00','739','fringilla ornare placerat,',44,44,44,44),(45,'2022-10-25 11:47:00','681','eu dui. Cum sociis',45,45,45,45),(46,'2023-02-07 12:18:00','262','sem.',46,46,46,46),(47,'2022-08-07 19:04:00','250','ac orci. Ut',47,47,47,47),(48,'2022-03-19 07:55:00','678','eu elit. Nulla facilisi. Sed',48,48,48,48),(49,'2021-07-11 16:21:00','78','odio. Nam interdum enim non nisi. Aenean eget',49,49,49,49),(50,'2022-11-25 03:24:00','223','massa. Integer vitae nibh.',50,50,50,50);
/*!40000 ALTER TABLE `historiek` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spelers`
--

DROP TABLE IF EXISTS `spelers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spelers` (
  `SpelersID` int NOT NULL,
  `Naam` varchar(100) NOT NULL,
  `Kaartnummer` int NOT NULL,
  `Datum gespeeld` datetime NOT NULL,
  PRIMARY KEY (`SpelersID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spelers`
--

LOCK TABLES `spelers` WRITE;
/*!40000 ALTER TABLE `spelers` DISABLE KEYS */;
INSERT INTO `spelers` VALUES (1,'Winter Hammond',2,'2022-08-10 12:19:00'),(2,'Ray Hodge',1,'2022-11-03 11:10:00'),(3,'Geoffrey Jackson',2,'2021-11-02 12:35:00'),(4,'Olivia George',1,'2022-04-14 06:08:00'),(5,'Quinlan Ward',2,'2023-01-24 08:48:00'),(6,'Katelyn Chambers',3,'2021-06-19 13:43:00'),(7,'Len Crane',1,'2022-06-17 05:48:00'),(8,'Rae Chang',5,'2021-09-17 02:06:00'),(9,'Gwendolyn Love',4,'2022-02-25 13:46:00'),(10,'Ivana Hester',3,'2022-08-09 20:11:00'),(11,'Baxter Osborne',1,'2022-06-09 16:50:00'),(12,'Macaulay Mckee',2,'2022-08-07 02:39:00'),(13,'Mariam Whitaker',2,'2022-01-29 10:48:00'),(14,'Karly Santiago',4,'2021-10-12 14:54:00'),(15,'Yetta Bass',1,'2022-05-22 03:10:00'),(16,'Ainsley Cain',5,'2021-12-21 08:18:00'),(17,'Zenia Hogan',4,'2022-02-07 07:13:00'),(18,'Roth Roberson',5,'2022-04-11 19:49:00'),(19,'Trevor Baxter',1,'2022-06-04 09:58:00'),(20,'Rooney Bonner',2,'2021-08-20 18:08:00'),(21,'Clayton Padilla',4,'2022-07-24 15:15:00'),(22,'Luke Nelson',1,'2021-11-16 22:49:00'),(23,'Maggie Glass',2,'2023-05-19 13:43:00'),(24,'Meghan Coleman',5,'2023-03-03 16:26:00'),(25,'Shea Guthrie',4,'2022-04-23 08:28:00'),(26,'Courtney Mcguire',1,'2022-02-14 10:12:00'),(27,'Buckminster Raymond',2,'2021-06-09 04:00:00'),(28,'Pearl Dorsey',3,'2021-06-20 20:05:00'),(29,'Hop Mckenzie',5,'2021-09-03 13:49:00'),(30,'Kuame Perez',5,'2022-06-02 04:40:00'),(31,'William Dean',3,'2022-07-23 19:29:00'),(32,'Pamela Leonard',1,'2022-03-15 04:08:00'),(33,'Caesar Mclaughlin',4,'2021-11-11 18:11:00'),(34,'Ifeoma Pitts',5,'2022-12-18 10:40:00'),(35,'Darryl Moreno',2,'2022-09-11 11:33:00'),(36,'Florence Mclaughlin',4,'2022-02-11 01:45:00'),(37,'Amanda Morse',4,'2021-09-28 14:36:00'),(38,'Violet Butler',2,'2021-11-23 14:21:00'),(39,'Whoopi Kennedy',4,'2023-01-02 07:07:00'),(40,'Odessa Quinn',2,'2023-05-03 23:58:00'),(41,'Kiona Cherry',3,'2023-03-15 12:26:00'),(42,'Patience Sherman',4,'2022-12-03 21:43:00'),(43,'Josiah Ramirez',2,'2023-03-03 11:33:00'),(44,'Aline Nixon',3,'2022-10-02 10:05:00'),(45,'Ivana Johns',5,'2021-12-14 00:30:00'),(46,'Baker Ross',3,'2022-10-06 15:40:00'),(47,'Lee Peck',5,'2023-04-18 23:39:00'),(48,'Palmer Rios',3,'2023-01-26 18:14:00'),(49,'Alice Snider',4,'2023-02-25 02:24:00'),(50,'Chava Parrish',2,'2022-07-04 15:26:00');
/*!40000 ALTER TABLE `spelers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vragen`
--

DROP TABLE IF EXISTS `vragen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vragen` (
  `vragenID` int NOT NULL,
  `vraag` varchar(100) NOT NULL,
  `antwoord` varchar(300) NOT NULL,
  PRIMARY KEY (`vragenID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vragen`
--

LOCK TABLES `vragen` WRITE;
/*!40000 ALTER TABLE `vragen` DISABLE KEYS */;
INSERT INTO `vragen` VALUES (1,'scelerisque, lorem ipsum sodales purus, in molestie tortor','Pellentesque tincidunt tempus risus. Donec egestas. Duis ac arcu. Nunc'),(2,'auctor velit. Aliquam nisl.','mauris elit, dictum eu, eleifend'),(3,'conubia nostra, per inceptos hymenaeos. Mauris ut','metus urna convallis erat, eget'),(4,'consequat, lectus sit','congue. In scelerisque scelerisque dui. Suspendisse ac metus vitae velit egestas'),(5,'ornare placerat, orci','id enim. Curabitur massa. Vestibulum accumsan'),(6,'neque tellus, imperdiet non, vestibulum','cursus vestibulum. Mauris magna. Duis dignissim tempor arcu. Vestibulum ut'),(7,'a, arcu. Sed et','Mauris non dui nec urna suscipit nonummy.'),(8,'Vivamus euismod urna.','tempus risus. Donec egestas. Duis ac arcu. Nunc mauris.'),(9,'et, eros. Proin ultrices. Duis volutpat nunc sit','lorem vitae odio sagittis semper. Nam tempor'),(10,'erat. Etiam vestibulum','Duis gravida. Praesent'),(11,'ultricies ligula. Nullam enim. Sed nulla ante, iaculis','Etiam imperdiet dictum magna.'),(12,'volutpat','adipiscing ligula. Aenean'),(13,'semper pretium neque. Morbi quis','dis parturient montes, nascetur ridiculus mus. Proin vel'),(14,'Etiam laoreet, libero','tempus scelerisque, lorem'),(15,'eu, accumsan sed, facilisis vitae, orci. Phasellus','dignissim pharetra.'),(16,'molestie tellus. Aenean egestas','Duis gravida.'),(17,'Morbi quis urna.','libero est, congue a, aliquet vel,'),(18,'lorem eu metus. In lorem. Donec elementum, lorem ut aliquam','Curabitur vel lectus. Cum sociis natoque penatibus et magnis dis'),(19,'ridiculus mus. Aenean','velit. Pellentesque ultricies dignissim lacus. Aliquam rutrum lorem'),(20,'est, congue a, aliquet vel, vulputate','in magna. Phasellus dolor elit,'),(21,'montes, nascetur ridiculus mus.','faucibus ut, nulla. Cras eu tellus eu augue porttitor interdum. Sed auctor'),(22,'ut, molestie in, tempus eu, ligula. Aenean euismod mauris','sit'),(23,'lacus, varius et, euismod et, commodo at, libero.','bibendum. Donec felis orci, adipiscing'),(24,'risus. Donec nibh enim, gravida sit amet, dapibus','Quisque purus sapien, gravida'),(25,'nec','Quisque ac libero nec'),(26,'dictum sapien. Aenean massa. Integer vitae nibh. Donec est','ac tellus. Suspendisse sed dolor. Fusce mi lorem, vehicula et,'),(27,'nisi. Aenean eget metus. In nec orci. Donec','hendrerit a, arcu.'),(28,'ipsum primis in faucibus orci luctus et ultrices','Curabitur consequat, lectus'),(29,'tempor augue ac ipsum.','fermentum vel, mauris. Integer sem elit, pharetra ut, pharetra'),(30,'mauris. Suspendisse aliquet molestie tellus. Aenean egestas hendrerit neque. In','Maecenas libero est, congue a, aliquet vel,'),(31,'non ante bibendum ullamcorper. Duis cursus, diam','facilisis lorem'),(32,'nec tellus.','feugiat. Sed nec metus facilisis lorem tristique aliquet.'),(33,'amet metus.','pretium et, rutrum non,'),(34,'parturient montes, nascetur ridiculus mus. Proin vel arcu','Duis gravida. Praesent eu nulla at sem molestie sodales. Mauris blandit'),(35,'montes, nascetur ridiculus mus. Donec dignissim magna','euismod est arcu ac orci. Ut semper pretium neque.'),(36,'arcu. Sed et libero. Proin mi. Aliquam gravida mauris ut','Morbi quis'),(37,'tellus, imperdiet non, vestibulum','fringilla cursus purus. Nullam scelerisque neque sed sem egestas blandit. Nam'),(38,'imperdiet, erat nonummy ultricies ornare, elit elit fermentum','leo. Vivamus nibh'),(39,'fermentum fermentum arcu. Vestibulum ante ipsum','pede, ultrices a, auctor non, feugiat nec, diam. Duis mi enim, condimentum'),(40,'ligula. Aenean gravida nunc sed pede. Cum sociis natoque','velit in aliquet lobortis, nisi nibh lacinia orci,'),(41,'luctus','semper tellus id nunc interdum feugiat. Sed nec metus facilisis'),(42,'iaculis quis, pede. Praesent eu dui.','erat neque non'),(43,'nec, malesuada ut, sem. Nulla interdum. Curabitur dictum.','ac facilisis facilisis, magna tellus'),(44,'mi lorem, vehicula et, rutrum eu, ultrices','leo. Cras vehicula'),(45,'accumsan laoreet ipsum. Curabitur consequat,','sed turpis nec mauris blandit mattis.'),(46,'Duis dignissim tempor arcu. Vestibulum ut','convallis est, vitae sodales'),(47,'Phasellus dapibus quam quis diam.','dui augue eu'),(48,'ullamcorper magna. Sed','Phasellus libero mauris, aliquam eu, accumsan sed, facilisis vitae, orci. Phasellus'),(49,'commodo at, libero.','purus. Nullam scelerisque neque sed sem egestas blandit. Nam'),(50,'imperdiet dictum magna. Ut tincidunt orci quis lectus. Nullam','per conubia nostra,');
/*!40000 ALTER TABLE `vragen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'puzzlebox'
--

--
-- Dumping routines for database 'puzzlebox'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-24  9:36:06
