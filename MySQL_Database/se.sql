-- ----------------------------
-- Table structure for se
-- ----------------------------
DROP TABLE IF EXISTS `se`;
CREATE TABLE `se` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sSourceIP` varchar(128) DEFAULT NULL COMMENT '源ip地址',
  `sMac` varchar(128) DEFAULT NULL COMMENT 'mac地址',
  `iBind` tinyint(2) DEFAULT NULL COMMENT ' 1为已绑定，0为未绑定',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of se
-- ----------------------------