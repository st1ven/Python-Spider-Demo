-- 导出 sentence 的数据库结构
CREATE DATABASE IF NOT EXISTS `sentence` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `sentence`;


-- 导出  表 sentence.sexy 结构
CREATE TABLE IF NOT EXISTS `sexy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(250) NOT NULL,
  `datetime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content` (`content`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;