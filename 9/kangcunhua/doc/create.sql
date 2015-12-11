create database kangcunhua;

use kangcunhua;

CREATE TABLE `stat_0` (
`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
`host` varchar(256) DEFAULT NULL,
`mem_free` int(11) DEFAULT NULL,
`mem_usage` int(11) DEFAULT NULL,
`mem_total` int(11) DEFAULT NULL,
`load_avg` varchar(128) DEFAULT NULL,
`time` bigint(11) DEFAULT NULL,
`user_define` varchar(4096) DEFAULT "",
PRIMARY KEY (`id`),
KEY `host` (`host`(255))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `stat_1` (
`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
`host` varchar(256) DEFAULT NULL,
`mem_free` int(11) DEFAULT NULL,
`mem_usage` int(11) DEFAULT NULL,
`mem_total` int(11) DEFAULT NULL,
`load_avg` varchar(128) DEFAULT NULL,
`time` bigint(11) DEFAULT NULL,
`user_define` varchar(4096) DEFAULT "",
PRIMARY KEY (`id`),
KEY `host` (`host`(255))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `stat_2` (
`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
`host` varchar(256) DEFAULT NULL,
`mem_free` int(11) DEFAULT NULL,
`mem_usage` int(11) DEFAULT NULL,
`mem_total` int(11) DEFAULT NULL,
`load_avg` varchar(128) DEFAULT NULL,
`time` bigint(11) DEFAULT NULL,
`user_define` varchar(4096) DEFAULT "",
PRIMARY KEY (`id`),
KEY `host` (`host`(255))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `stat_3` (
`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
`host` varchar(256) DEFAULT NULL,
`mem_free` int(11) DEFAULT NULL,
`mem_usage` int(11) DEFAULT NULL,
`mem_total` int(11) DEFAULT NULL,
`load_avg` varchar(128) DEFAULT NULL,
`time` bigint(11) DEFAULT NULL,
`user_define` varchar(4096) DEFAULT "",
PRIMARY KEY (`id`),
KEY `host` (`host`(255))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

show tables;