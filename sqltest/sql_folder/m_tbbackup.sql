/*
Navicat MySQL Data Transfer

Source Server         : 3.123
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : db_firewall

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2016-09-14 18:19:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for m_tbbackup
-- ----------------------------
DROP TABLE IF EXISTS `m_tbbackup`;
CREATE TABLE `m_tbbackup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sName` varchar(150) CHARACTER SET latin1 DEFAULT NULL,
  `sPath` varchar(200) CHARACTER SET latin1 DEFAULT NULL,
  `iTime` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of m_tbbackup
-- ----------------------------
