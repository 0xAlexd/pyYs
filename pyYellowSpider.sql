-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Ven 28 Octobre 2016 à 03:59
-- Version du serveur :  5.6.17
-- Version de PHP :  5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

-- Structure de la table `ys2languages`

--CREATE TABLE IF NOT EXISTS `ys2languages` (`id` int(11) NOT NULL AUTO_INCREMENT,`html_code` varchar(10) NOT NULL,`language` varchar(254) NOT NULL,`pays` varchar(254) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=200 ;

-- Structure de la table `ys2mails`

CREATE TABLE IF NOT EXISTS `ys2mails` (`id` int(11) NOT NULL AUTO_INCREMENT,`mail` varchar(254) NOT NULL,`id_website` int(11) NOT NULL,`date` int(10) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4012 ;

-- Structure de la table `ys2sc_detail`

CREATE TABLE IF NOT EXISTS `ys2sc_detail` (`id` int(11) NOT NULL AUTO_INCREMENT,`scan_id` varchar(15) NOT NULL,`page` varchar(254) NOT NULL,`type_lien` int(1) NOT NULL,`checked` int(11) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14408 ;

-- Structure de la table `ys2sc_img`

CREATE TABLE IF NOT EXISTS `ys2sc_img` (`id` int(11) NOT NULL AUTO_INCREMENT,`scan_id` varchar(15) NOT NULL,`page` varchar(254) NOT NULL,`link` varchar(254) NOT NULL,`link_type` int(1) NOT NULL,`local_link` varchar(254) NOT NULL,`size` varchar(254) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=37523 ;

-- Structure de la table `ys2sc_scan`

CREATE TABLE IF NOT EXISTS `ys2sc_scan` (`id` int(11) NOT NULL AUTO_INCREMENT,`scan_id` varchar(15) NOT NULL,`website` varchar(254) NOT NULL,`date` int(9) NOT NULL,`result` int(11) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

-- Structure de la table `ys2websites`

CREATE TABLE IF NOT EXISTS `ys2websites` (`id` int(11) NOT NULL AUTO_INCREMENT,`website` varchar(254) NOT NULL,`extension` varchar(5) NOT NULL,`title` varchar(254) NOT NULL,`description` varchar(254) NOT NULL,`languageCode` varchar(254) NOT NULL,`checked` tinyint(4) NOT NULL,`mail_count` int(11) NOT NULL,`date` int(10) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=26966 ;

--INSERT INTO 'ys2websites' VALUES(0,'', '', '', '', '', 0, 0, 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
