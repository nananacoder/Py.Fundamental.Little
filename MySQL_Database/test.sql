/*
Navicat MySQL Data Transfer

Source Server         : 172.172.2.240_3306
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : db_firewall

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2016-09-07 09:37:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for m_blacklist
-- ----------------------------
DROP TABLE IF EXISTS `m_blacklist`;
CREATE TABLE `m_blacklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sSourceAddr` varchar(64) DEFAULT NULL COMMENT '来源地址',
  `sStopReason` varchar(256) DEFAULT NULL COMMENT '禁止原因',
  `iStopTime` int(11) DEFAULT NULL COMMENT '禁止时间',
  `iStatus` varchar(4) DEFAULT NULL,
  `iTime` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='黑名单';

-- ----------------------------
-- Records of m_blacklist
-- ----------------------------

-- ----------------------------
-- Table structure for m_IPS_template_rules
-- ----------------------------
DROP TABLE IF EXISTS `m_IPS_template_rules`;
CREATE TABLE `m_IPS_template_rules` (
  `id` int(11) NOT NULL,
  `iSID` int(11) NOT NULL,
  `sRules` text,
  PRIMARY KEY (`iSID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of m_IPS_template_rules
-- ----------------------------

-- ----------------------------
-- Table structure for m_tbaccount
-- ----------------------------
DROP TABLE IF EXISTS `m_tbaccount`;
CREATE TABLE `m_tbaccount` (
  `iUserId` bigint(20) NOT NULL AUTO_INCREMENT,
  `sLoginAccount` varchar(50) NOT NULL,
  `sPasswd` varchar(32) NOT NULL,
  `sUerName` varchar(50) DEFAULT NULL,
  `sRole` bigint(12) NOT NULL,
  `iGender` tinyint(1) DEFAULT NULL COMMENT '0�?�?',
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `iInsertDate` int(11) DEFAULT NULL,
  `iUpdateDate` int(11) DEFAULT NULL,
  `iStatus` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1启用2禁用',
  `iOperationUserId` bigint(20) NOT NULL DEFAULT '0',
  `iOnline` tinyint(1) DEFAULT '0' COMMENT '0下线1在线',
  `iUpdatePwd` int(11) DEFAULT '0',
  `usb_key` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否启用USB_KEY',
  `usb_pin` varchar(20) NOT NULL DEFAULT 'bluedon' COMMENT '使用USBKEY后的 USB PIN',
  PRIMARY KEY (`iUserId`)
) ENGINE=MyISAM AUTO_INCREMENT=3983 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of m_tbaccount
-- ----------------------------
INSERT INTO `m_tbaccount` VALUES ('1', 'root', '4ec39b66d9436a25c88b280b37ff92b8', 'root', '0', null, null, null, null, '0', '1461139512', '4', '0', '1', '1471139512', '0', 'bluedon');
INSERT INTO `m_tbaccount` VALUES ('1483', 'secadmin', 'a1ac8ddaf95ba4de6925d656500ffad3', 'secadmin', '3', null, null, null, null, '1453084510', '1468369680', '4', '0', '0', '1478369680', '0', 'bluedon');
INSERT INTO `m_tbaccount` VALUES ('1485', 'audit', '483849c4c8d8fe2f6cec2360921b7099', 'audit', '2', null, null, null, null, '1453084720', '1468369690', '4', '0', '0', '1478369690', '0', 'bluedon');
INSERT INTO `m_tbaccount` VALUES ('456', 'admin', '4022be391c9ab40996e2aeb217253252', 'admin', '1', null, null, null, null, '1458035971', '1468369476', '4', '0', '1', '1478369476', '0', 'bluedon');

-- ----------------------------
-- Table structure for m_tbwebapplication_lib
-- ----------------------------
DROP TABLE IF EXISTS `m_tbwebapplication_lib`;
CREATE TABLE `m_tbwebapplication_lib` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sRuleID` varchar(128) DEFAULT NULL COMMENT '规则ID',
  `sRealID` varchar(128) DEFAULT NULL COMMENT '后台操作id',
  `iPriority` tinyint(2) DEFAULT NULL COMMENT '优先级',
  `sRuleName` varchar(512) DEFAULT NULL COMMENT '规则名称',
  `sDesc` text COMMENT '说明',
  `sType` varchar(128) DEFAULT NULL COMMENT '类型',
  `sDangerLever` varchar(64) DEFAULT NULL COMMENT '危险等级',
  `sInterceptionMethod` varchar(64) DEFAULT NULL COMMENT '拦截方式',
  `sHttpRequestType` varchar(64) DEFAULT NULL COMMENT 'HTTP请求类型',
  `sMatchAlgorithm` varchar(64) DEFAULT NULL COMMENT '匹配算法',
  `sMatchContent` varchar(64) DEFAULT NULL COMMENT '匹配内容',
  `sFeatureKey` varchar(512) DEFAULT NULL COMMENT '正则表达式字符串',
  `iStatus` tinyint(2) DEFAULT NULL COMMENT '状态，1开启，0关闭',
  `iUpdateTime` int(11) DEFAULT NULL COMMENT '更新时间 ',
  `iCustomOrInset` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='web应用防护规则库';

-- ----------------------------
-- Records of m_tbwebapplication_lib
-- ----------------------------
