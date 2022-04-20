/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 100414
Source Host           : localhost:3306
Source Database       : gar

Target Server Type    : MYSQL
Target Server Version : 100414
File Encoding         : 65001

Date: 2022-01-09 19:47:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for addfrend
-- ----------------------------
DROP TABLE IF EXISTS `addfrend`;
CREATE TABLE `addfrend` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) NOT NULL,
  `to_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `from_id` (`from_id`),
  KEY `to_id` (`to_id`),
  CONSTRAINT `addfrend_ibfk_1` FOREIGN KEY (`from_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `addfrend_ibfk_2` FOREIGN KEY (`to_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of addfrend
-- ----------------------------
INSERT INTO `addfrend` VALUES ('25', '12', '9');
INSERT INTO `addfrend` VALUES ('26', '12', '6');
INSERT INTO `addfrend` VALUES ('27', '12', '5');
INSERT INTO `addfrend` VALUES ('28', '12', '5');
INSERT INTO `addfrend` VALUES ('29', '12', '6');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `post_id` (`post_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comment
-- ----------------------------

-- ----------------------------
-- Table structure for drug
-- ----------------------------
DROP TABLE IF EXISTS `drug`;
CREATE TABLE `drug` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_1_id` int(11) NOT NULL,
  `user_2_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_1_id` (`user_1_id`),
  KEY `user_2_id` (`user_2_id`),
  CONSTRAINT `drug_ibfk_1` FOREIGN KEY (`user_1_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `drug_ibfk_2` FOREIGN KEY (`user_2_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of drug
-- ----------------------------
INSERT INTO `drug` VALUES ('12', '11', '12');
INSERT INTO `drug` VALUES ('13', '13', '8');
INSERT INTO `drug` VALUES ('14', '11', '3');
INSERT INTO `drug` VALUES ('15', '11', '5');
INSERT INTO `drug` VALUES ('16', '11', '8');
INSERT INTO `drug` VALUES ('17', '11', '12');
INSERT INTO `drug` VALUES ('18', '11', '2');
INSERT INTO `drug` VALUES ('19', '11', '14');
INSERT INTO `drug` VALUES ('20', '12', '2');
INSERT INTO `drug` VALUES ('21', '12', '11');
INSERT INTO `drug` VALUES ('22', '13', '2');
INSERT INTO `drug` VALUES ('23', '12', '5');
INSERT INTO `drug` VALUES ('24', '12', '8');
INSERT INTO `drug` VALUES ('25', '14', '13');

-- ----------------------------
-- Table structure for like
-- ----------------------------
DROP TABLE IF EXISTS `like`;
CREATE TABLE `like` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `like_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `like_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of like
-- ----------------------------

-- ----------------------------
-- Table structure for messages
-- ----------------------------
DROP TABLE IF EXISTS `messages`;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) NOT NULL,
  `to_id` int(11) NOT NULL,
  `message` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`from_id`),
  KEY `drug_id` (`to_id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`from_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `messages_ibfk_3` FOREIGN KEY (`to_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of messages
-- ----------------------------
INSERT INTO `messages` VALUES ('7', '12', '5', 'gfghfghfgh', '');
INSERT INTO `messages` VALUES ('8', '12', '2', 'k,k,k,k,k,k,', '');
INSERT INTO `messages` VALUES ('9', '12', '5', 'bnbnbn', '');
INSERT INTO `messages` VALUES ('10', '14', '13', 'barev', '');
INSERT INTO `messages` VALUES ('11', '13', '14', 'jakjskajs', '');
INSERT INTO `messages` VALUES ('12', '14', '13', 'amskas', '');
INSERT INTO `messages` VALUES ('13', '13', '14', 'sklakls', '');
INSERT INTO `messages` VALUES ('14', '14', '13', 'Anna', '');
INSERT INTO `messages` VALUES ('15', '13', '14', 'narek', '');
INSERT INTO `messages` VALUES ('16', '13', '14', 'ajsahj', '');
INSERT INTO `messages` VALUES ('17', '14', '13', 'lkjkjj', '');
INSERT INTO `messages` VALUES ('18', '13', '14', 'mmmmmmm', '');
INSERT INTO `messages` VALUES ('19', '13', '14', 'asdfgjkl;', '');
INSERT INTO `messages` VALUES ('20', '13', '14', 'cvzcvx', '');
INSERT INTO `messages` VALUES ('21', '13', '14', 'new message', '');
INSERT INTO `messages` VALUES ('22', '14', '13', 'barev1', '');
INSERT INTO `messages` VALUES ('23', '13', '14', '09.01', '');

-- ----------------------------
-- Table structure for photo
-- ----------------------------
DROP TABLE IF EXISTS `photo`;
CREATE TABLE `photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `photo_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of photo
-- ----------------------------
INSERT INTO `photo` VALUES ('42', 'images/21231633467user.jpg', '12');
INSERT INTO `photo` VALUES ('43', 'images/36177091866user-6.jpg', '12');
INSERT INTO `photo` VALUES ('44', 'images/5252936107user-3.jpg', '12');
INSERT INTO `photo` VALUES ('45', 'images/32557177421user1.png', '12');
INSERT INTO `photo` VALUES ('46', 'images/50163830409user-5.jpg', '12');
INSERT INTO `photo` VALUES ('48', 'images/96936700400user-3.jpg', '12');

-- ----------------------------
-- Table structure for posts
-- ----------------------------
DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(255) NOT NULL,
  `img_url` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,
  `time` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of posts
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `photo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('2', 'ana', 'dsgsgsgsdg', 'Men', '43', 'ani@gmail.com', '$2b$12$h41dUIkQISUrkNgcoFwYReaVBiiE9eG4z.hbgTt.cKGT2Mb39a9TW', 'images/users/user1.png');
INSERT INTO `user` VALUES ('3', 'name', 'surname', 'gender', '26', 'emile@mail.ru', '$2b$12$h41dUIkQISUrkNgcoFwYReaVBiiE9eG4z.hbgTt.cKGT2Mb39a9TW', 'images/users/user1.png');
INSERT INTO `user` VALUES ('4', 'ana', 'asdksjadm', 'Men', '43', 'ani@gmail.com', '$2b$12$FMrYo0tE7hbhsTPfwxpV3OfLZx2ZhqNQdbh4Ec5Z4g1ZAe3.doo02', 'images/users/user1.png');
INSERT INTO `user` VALUES ('5', 'Garik', 'Atanasyan', 'Men', '26', 'Atanasyan.2016@mail.ru', '$2b$12$nKPy1/MrKdlV6Fmyw5v03uJchLRrXs59dbdUpX4mvX5mqVEXtoaB.', 'images/users/user1.png');
INSERT INTO `user` VALUES ('6', 'Garik', 'Atanasyan', 'Men', '26', 'Atanasyan.2016@mail.ru', '$2b$12$zRILwXn3fgZK/ckiT6ZBEeL.554muh/tC6Wol1gaIHQm3zSUx3SVG', 'images/users/user1.png');
INSERT INTO `user` VALUES ('7', 'ana', 'lasjkdasklj', 'Female', '43', 'ani@gmail.com', '$2b$12$ohtNktFsayWZpeQK7RexNuHvRb.cqRhiFEAgv9ccO8xaSgRcFUQ9m', 'images/users/user1.png');
INSERT INTO `user` VALUES ('8', 'Sona Atana', 'dfgdfg', 'Male', '25', 'gano1995@mail.ru', '$2b$12$tEB7FYp5bDIIcuAnJJYZfuG5PScSKU4MzTcyMwHPUuTfkEuDtUmnG', 'images/users/user1.png');
INSERT INTO `user` VALUES ('9', 'Garik', 'Atanasyan', 'Male', '25', 'gano1995@mail.ru', '$2b$12$tEB7FYp5bDIIcuAnJJYZfuG5PScSKU4MzTcyMwHPUuTfkEuDtUmnG', 'images/users/user1.png');
INSERT INTO `user` VALUES ('10', 'Ani', 'Sargsyan', 'Female', '25', 'ani@gmail.com', '$2b$12$wOH8LKSih4gQ2mSKRXjk4eeVQBgYlqNzK2G.X/hL2bVba82u58uWO', 'images/users/user1.png');
INSERT INTO `user` VALUES ('11', 'Anna', 'Sargsyan', 'Female', '12', 'anna@gmail.com', '$2b$12$h41dUIkQISUrkNgcoFwYReaVBiiE9eG4z.hbgTt.cKGT2Mb39a9TW', 'images/users/user1.png');
INSERT INTO `user` VALUES ('12', 'Gar', 'Atanasyan', 'Male', '26', 'Garik@mail.ru', '$2b$12$tEB7FYp5bDIIcuAnJJYZfuG5PScSKU4MzTcyMwHPUuTfkEuDtUmnG', 'images/21231633467user.jpg');
INSERT INTO `user` VALUES ('13', 'qwertyui', 'asdfghj', 'Female', '25', 'aram@mail.ru', '$2b$12$5gu.qw.j7JS.ZR6av0d4k.HdLNRHhYnouFQYPH3xZoWaL/4ouVHIC', 'images/users/user1.png');
INSERT INTO `user` VALUES ('14', 'zxcvbn', 'zxcvbn', 'Female', '25', 'aram1@mail.ru', '$2b$12$YQHWwjtNF/NcvJuOTcxVm.6xzP8cKMaWx6A3yb6sELVbGAFuAcdWC', 'images/users/user1.png');
SET FOREIGN_KEY_CHECKS=1;
