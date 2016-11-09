/*
Navicat MySQL Data Transfer

Source Server         : 3.123
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : db_firewall

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2016-09-14 18:19:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for m_tbaddress_list
-- ----------------------------
DROP TABLE IF EXISTS `m_tbaddress_list`;
CREATE TABLE `m_tbaddress_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sAddressname` varchar(255) DEFAULT NULL,
  `sAddress` varchar(512) DEFAULT NULL COMMENT '地址',
  `sIPV` varchar(32) DEFAULT NULL COMMENT '地址类型，ipv4，ipv6',
  `sNetmask` varchar(255) DEFAULT NULL COMMENT '掩码位数',
  `sAddtype` varchar(255) DEFAULT NULL COMMENT '地址类型，1：单ip，2：ip段',
  `sMark` varchar(255) DEFAULT NULL COMMENT '备注',
  `sInserttime` varchar(12) DEFAULT NULL,
  `sUpdatetime` varchar(12) DEFAULT NULL,
  `IpgroupId` int(11) DEFAULT NULL COMMENT '用户组ID',
  `sIPJson` varchar(255) DEFAULT NULL COMMENT '根据ip的类型,存放相应的json值.''iprange'':ip区间;''ipmaskrange_str'': 十进制ip掩码(1.1.1.0/255.255.255.0);''ipmaskrange_int'': 二进制ip掩码(1.1.1.0/24);''ipmaskalone_str'':十进制ip;''ipmaskalone_int'':二进制ip',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='地址管理-地址列表';

-- ----------------------------
-- Records of m_tbaddress_list
-- ----------------------------
INSERT INTO `m_tbaddress_list` VALUES ('1', '192.168.11.0/24', '192.168.11.0', 'ipv4', '24', '1', '', null, null, null, '{\"ipmaskrange_str\": \"192.168.11.0/255.255.255.0\", \"ipmaskrange_int\": \"192.168.11.0/24\"}');
