/*
Navicat MySQL Data Transfer

Source Server         : 3.123
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : db_firewall

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2016-09-14 18:19:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for m_tbbsservice
-- ----------------------------
DROP TABLE IF EXISTS `m_tbbsservice`;
CREATE TABLE `m_tbbsservice` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `sBsServiceName` varchar(400) DEFAULT NULL,
  `iAgreement` tinyint(2) NOT NULL COMMENT '协议，1为HTTP，2为HTTPS',
  `sBsServiceAddr` varchar(100) NOT NULL COMMENT '服务器地址',
  `sAuthentication` tinyint(2) DEFAULT NULL COMMENT '认证，1为匿名访问，2为通过口令访问，3通过证书访问，4通过双因素访问',
  `sMark` varchar(400) DEFAULT NULL COMMENT '备注',
  `iCsStatus` tinyint(2) DEFAULT NULL COMMENT 'C/S支持',
  `iMdLevel` tinyint(2) DEFAULT NULL COMMENT '加密强度：1为高，2为中，3为低',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of m_tbbsservice
-- ----------------------------
