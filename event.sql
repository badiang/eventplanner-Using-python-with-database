-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 07, 2019 at 08:07 AM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `event`
--

-- --------------------------------------------------------

--
-- Table structure for table `saveData`
--

CREATE TABLE `saveData` (
  `id` int(11) NOT NULL,
  `wat` varchar(500) NOT NULL,
  `wen` date NOT NULL,
  `wer` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `saveData`
--

INSERT INTO `saveData` (`id`, `wat`, `wen`, `wer`) VALUES
(4, 'eating contest', '2018-06-18', 'mobod'),
(6, 'easting contest', '2018-04-11', 'mobod'),
(7, 'networking exam', '2018-11-09', 'mobod'),
(8, 'eating contest', '2018-05-11', 'mobod');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `saveData`
--
ALTER TABLE `saveData`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `saveData`
--
ALTER TABLE `saveData`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
