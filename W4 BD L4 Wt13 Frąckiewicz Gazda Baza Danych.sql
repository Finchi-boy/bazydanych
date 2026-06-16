-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 16, 2026 at 11:56 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rekrutacjak`
--

-- --------------------------------------------------------

--
-- Table structure for table `Aplikacje`
--

CREATE TABLE `Aplikacje` (
  `IdKandydata` int(11) NOT NULL,
  `IdKierunku` int(11) NOT NULL,
  `DataZgloszenia` text DEFAULT NULL,
  `Punkty` double DEFAULT 0,
  `Oplata` double DEFAULT 0,
  `StatusA` text DEFAULT 'złożona',
  `Priorytet` int(11) DEFAULT 1,
  `IdPracownika` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Aplikacje`
--

INSERT INTO `Aplikacje` (`IdKandydata`, `IdKierunku`, `DataZgloszenia`, `Punkty`, `Oplata`, `StatusA`, `Priorytet`, `IdPracownika`) VALUES
(1, 1, '2025-06-01', 307.5, 85, 'przyjety', 1, 1),
(1, 2, '2026-06-16', 187.5, 0, 'złożona', 1, NULL),
(1, 3, '2025-06-01', 307.5, 85, 'przyjety', 2, 1),
(2, 2, '2025-06-02', 182, 85, 'przyjety', 1, 1),
(3, 1, '2025-06-01', 328, 85, 'przyjety', 1, 2),
(4, 1, '2025-06-03', 0, 85, 'przyjety', 1, 1),
(5, 1, '2025-06-02', 105, 85, 'przyjety', 1, 1),
(5, 2, '2025-06-02', 105, 85, 'przyjety', 2, 1),
(6, 5, '2026-06-16', 0, 0, 'przyjety', 1, 1),
(6, 6, '2026-06-16', 0, 0, 'przyjety', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Egzaminy`
--

CREATE TABLE `Egzaminy` (
  `IdEgzaminu` int(11) NOT NULL,
  `NazwaE` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Egzaminy`
--

INSERT INTO `Egzaminy` (`IdEgzaminu`, `NazwaE`) VALUES
(1, 'Matematyka rozszerzona'),
(2, 'Fizyka rozszerzona'),
(3, 'Informatyka rozszerzona'),
(4, 'Język angielski rozszerzony');

-- --------------------------------------------------------

--
-- Table structure for table `Kandydaci`
--

CREATE TABLE `Kandydaci` (
  `IdKandydata` int(11) NOT NULL,
  `Nazwisko` text NOT NULL,
  `Imie` text NOT NULL,
  `DrugieImie` text DEFAULT NULL,
  `Pesel` text NOT NULL,
  `DataUrodzenia` text DEFAULT NULL,
  `Telefon` text DEFAULT NULL,
  `Email` text NOT NULL,
  `Haslo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Kandydaci`
--

INSERT INTO `Kandydaci` (`IdKandydata`, `Nazwisko`, `Imie`, `DrugieImie`, `Pesel`, `DataUrodzenia`, `Telefon`, `Email`, `Haslo`) VALUES
(1, 'Frąckiewicz', 'Maciej', 'Krzysztof', '05221207652', '2005-12-02', '572484522', 'maciekf05@gmail.com', 'test.05'),
(2, 'Nowak', 'Julia', 'Maria', '04050367890', '2004-05-03', '502345678', 'julia.nowak@gmail.com', 'haslo123'),
(3, 'Wiśniewska', 'Katarzyna', NULL, '03121598765', '2003-12-15', '503456789', 'k.wisniewska@gmail.com', 'haslo123'),
(4, 'Zając', 'Tomasz', NULL, '04070412345', '2004-07-04', '504567890', 'tomasz.zajac@gmail.com', 'haslo123'),
(5, 'Lewandowski', 'Michał', 'Jan', '04030434132', '2003-09-15', '505678901', 'm.lewandowski@gmail.com', 'haslo123'),
(6, 'Frąckiewicz', 'Maciej', '', '05130322037', '2005-12-02', '', 'frackiewicz.lo3@gmail.com', 'pass');

-- --------------------------------------------------------

--
-- Table structure for table `Kierunki`
--

CREATE TABLE `Kierunki` (
  `IdKierunku` int(11) NOT NULL,
  `Nazwa` text NOT NULL,
  `Symbol` text DEFAULT NULL,
  `Poziom` text DEFAULT NULL,
  `LimitMiejsc` int(11) DEFAULT NULL,
  `IdWydzialu` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Kierunki`
--

INSERT INTO `Kierunki` (`IdKierunku`, `Nazwa`, `Symbol`, `Poziom`, `LimitMiejsc`, `IdWydzialu`) VALUES
(1, 'Informatyka', 'INF', 'inżynierskie', 120, 1),
(2, 'Informatyka stosowana', 'INS', 'inżynierskie', 80, 1),
(3, 'Cyberbezpieczeństwo', 'CYB', 'inżynierskie', 60, 1),
(4, 'Matematyka stosowana', 'MAS', 'inżynierskie', 50, 2),
(5, 'Elektronika i telekomunikacja', 'ELT', 'inżynierskie', 90, 3),
(6, 'Informatyka', 'INF-M', 'magisterskie', 40, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Osiagniecia`
--

CREATE TABLE `Osiagniecia` (
  `IdOsiagniecia` int(11) NOT NULL,
  `Nazwa` text NOT NULL,
  `Tytul` text DEFAULT NULL,
  `Punkty` double DEFAULT 0,
  `Status` text DEFAULT 'oczekujacy',
  `IdKandydata` int(11) DEFAULT NULL,
  `IdPracownika` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Osiagniecia`
--

INSERT INTO `Osiagniecia` (`IdOsiagniecia`, `Nazwa`, `Tytul`, `Punkty`, `Status`, `IdKandydata`, `IdPracownika`) VALUES
(1, 'Olimpiada Informatyczna', 'Laureat etapu okręgowego', 15, 'zatwierdzony', 1, 1),
(2, 'Olimpiada Matematyczna', 'Finalista', 10, 'zatwierdzony', 2, 2),
(3, 'Certyfikat językowy', 'Cambridge C1', 5, 'oczekujacy', 3, NULL),
(4, 'Hackhaton PWR', 'II miejsce', 8, 'oczekujacy', 4, NULL),
(5, 'Olimpiada Fizyczna', 'Laureat etapu okręgowego', 15, 'zatwierdzony', 5, 1),
(6, 'test', 'testowy', 15, 'zatwierdzony', 6, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Pracownicy`
--

CREATE TABLE `Pracownicy` (
  `IdPracownika` int(11) NOT NULL,
  `Nazwisko` text NOT NULL,
  `Imie` text NOT NULL,
  `Email` text NOT NULL,
  `Haslo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Pracownicy`
--

INSERT INTO `Pracownicy` (`IdPracownika`, `Nazwisko`, `Imie`, `Email`, `Haslo`) VALUES
(1, 'Frąckiewicz', 'Maciej', 'maciekf05@gmail.com', 'AdminPass'),
(2, 'Nowak', 'Anna', 'anna.nowak@pwr.edu.pl', 'admin123'),
(3, 'Wiśniewski', 'Piotr', 'p.wisniewski@pwr.edu.pl', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `Przeliczniki`
--

CREATE TABLE `Przeliczniki` (
  `IdEgzaminu` int(11) NOT NULL,
  `IdKierunku` int(11) NOT NULL,
  `Mnoznik` double DEFAULT 1,
  `Minimum` double DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Przeliczniki`
--

INSERT INTO `Przeliczniki` (`IdEgzaminu`, `IdKierunku`, `Mnoznik`, `Minimum`) VALUES
(1, 1, 1.5, 40),
(1, 2, 1.5, 40),
(1, 3, 1.5, 40),
(1, 4, 2, 50),
(1, 5, 1.5, 40),
(2, 1, 1, 0),
(2, 4, 1.5, 30),
(2, 5, 2, 35),
(3, 1, 2, 30),
(3, 2, 2, 30),
(3, 3, 2.5, 35);

-- --------------------------------------------------------

--
-- Table structure for table `Wydzialy`
--

CREATE TABLE `Wydzialy` (
  `IdWydzialu` int(11) NOT NULL,
  `Nazwa` text NOT NULL,
  `Adres` text DEFAULT NULL,
  `Symbol` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Wydzialy`
--

INSERT INTO `Wydzialy` (`IdWydzialu`, `Nazwa`, `Adres`, `Symbol`) VALUES
(1, 'Wydział Informatyki i Telekomunikacji', 'ul. Wybrzeże Wyspiańskiego 27, Wrocław', 'W4'),
(2, 'Wydział Matematyki', 'ul. Wybrzeże Wyspiańskiego 27, Wrocław', 'W13'),
(3, 'Wydział Elektroniki', 'ul. Wybrzeże Wyspiańskiego 27, Wrocław', 'W4N');

-- --------------------------------------------------------

--
-- Table structure for table `Wyniki`
--

CREATE TABLE `Wyniki` (
  `IdKandydata` int(11) NOT NULL,
  `IdEgzaminu` int(11) NOT NULL,
  `Wartosc` double DEFAULT NULL,
  `StatusWN` text DEFAULT 'oczekujacy',
  `IdPracownika` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Wyniki`
--

INSERT INTO `Wyniki` (`IdKandydata`, `IdEgzaminu`, `Wartosc`, `StatusWN`, `IdPracownika`) VALUES
(1, 1, 5, 'zatwierdzony', 1),
(1, 3, 90, 'zatwierdzony', 1),
(1, 4, 72, 'zatwierdzony', NULL),
(2, 1, 78, 'zatwierdzony', 1),
(2, 2, 65, 'zatwierdzony', 2),
(2, 4, 88, 'zatwierdzony', NULL),
(3, 1, 92, 'zatwierdzony', 1),
(3, 3, 95, 'zatwierdzony', 2),
(4, 1, 60, 'oczekujacy', NULL),
(4, 2, 55, 'oczekujacy', NULL),
(5, 1, 70, 'zatwierdzony', 1),
(5, 3, 75, 'oczekujacy', NULL),
(6, 1, 100, 'zatwierdzony', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Aplikacje`
--
ALTER TABLE `Aplikacje`
  ADD PRIMARY KEY (`IdKandydata`,`IdKierunku`),
  ADD KEY `Aplikacje_FK_0_0` (`IdPracownika`),
  ADD KEY `Aplikacje_FK_1_0` (`IdKierunku`);

--
-- Indexes for table `Egzaminy`
--
ALTER TABLE `Egzaminy`
  ADD PRIMARY KEY (`IdEgzaminu`),
  ADD UNIQUE KEY `sqlite_autoindex_Egzaminy_1` (`NazwaE`(255));

--
-- Indexes for table `Kandydaci`
--
ALTER TABLE `Kandydaci`
  ADD PRIMARY KEY (`IdKandydata`),
  ADD UNIQUE KEY `sqlite_autoindex_Kandydaci_2` (`Email`(255)),
  ADD UNIQUE KEY `sqlite_autoindex_Kandydaci_1` (`Pesel`(255));

--
-- Indexes for table `Kierunki`
--
ALTER TABLE `Kierunki`
  ADD PRIMARY KEY (`IdKierunku`),
  ADD KEY `Kierunki_FK_0_0` (`IdWydzialu`);

--
-- Indexes for table `Osiagniecia`
--
ALTER TABLE `Osiagniecia`
  ADD PRIMARY KEY (`IdOsiagniecia`),
  ADD KEY `Osiagniecia_FK_0_0` (`IdPracownika`),
  ADD KEY `Osiagniecia_FK_1_0` (`IdKandydata`);

--
-- Indexes for table `Pracownicy`
--
ALTER TABLE `Pracownicy`
  ADD PRIMARY KEY (`IdPracownika`),
  ADD UNIQUE KEY `sqlite_autoindex_Pracownicy_1` (`Email`(255));

--
-- Indexes for table `Przeliczniki`
--
ALTER TABLE `Przeliczniki`
  ADD PRIMARY KEY (`IdEgzaminu`,`IdKierunku`),
  ADD KEY `Przeliczniki_FK_0_0` (`IdKierunku`);

--
-- Indexes for table `Wydzialy`
--
ALTER TABLE `Wydzialy`
  ADD PRIMARY KEY (`IdWydzialu`);

--
-- Indexes for table `Wyniki`
--
ALTER TABLE `Wyniki`
  ADD PRIMARY KEY (`IdKandydata`,`IdEgzaminu`),
  ADD KEY `Wyniki_FK_0_0` (`IdPracownika`),
  ADD KEY `Wyniki_FK_1_0` (`IdEgzaminu`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Egzaminy`
--
ALTER TABLE `Egzaminy`
  MODIFY `IdEgzaminu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Kandydaci`
--
ALTER TABLE `Kandydaci`
  MODIFY `IdKandydata` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Kierunki`
--
ALTER TABLE `Kierunki`
  MODIFY `IdKierunku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Osiagniecia`
--
ALTER TABLE `Osiagniecia`
  MODIFY `IdOsiagniecia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Pracownicy`
--
ALTER TABLE `Pracownicy`
  MODIFY `IdPracownika` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Wydzialy`
--
ALTER TABLE `Wydzialy`
  MODIFY `IdWydzialu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Aplikacje`
--
ALTER TABLE `Aplikacje`
  ADD CONSTRAINT `Aplikacje_FK_0_0` FOREIGN KEY (`IdPracownika`) REFERENCES `Pracownicy` (`IdPracownika`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Aplikacje_FK_1_0` FOREIGN KEY (`IdKierunku`) REFERENCES `Kierunki` (`IdKierunku`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Aplikacje_FK_2_0` FOREIGN KEY (`IdKandydata`) REFERENCES `Kandydaci` (`IdKandydata`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Kierunki`
--
ALTER TABLE `Kierunki`
  ADD CONSTRAINT `Kierunki_FK_0_0` FOREIGN KEY (`IdWydzialu`) REFERENCES `Wydzialy` (`IdWydzialu`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Osiagniecia`
--
ALTER TABLE `Osiagniecia`
  ADD CONSTRAINT `Osiagniecia_FK_0_0` FOREIGN KEY (`IdPracownika`) REFERENCES `Pracownicy` (`IdPracownika`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Osiagniecia_FK_1_0` FOREIGN KEY (`IdKandydata`) REFERENCES `Kandydaci` (`IdKandydata`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Przeliczniki`
--
ALTER TABLE `Przeliczniki`
  ADD CONSTRAINT `Przeliczniki_FK_0_0` FOREIGN KEY (`IdKierunku`) REFERENCES `Kierunki` (`IdKierunku`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Przeliczniki_FK_1_0` FOREIGN KEY (`IdEgzaminu`) REFERENCES `Egzaminy` (`IdEgzaminu`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Wyniki`
--
ALTER TABLE `Wyniki`
  ADD CONSTRAINT `Wyniki_FK_0_0` FOREIGN KEY (`IdPracownika`) REFERENCES `Pracownicy` (`IdPracownika`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Wyniki_FK_1_0` FOREIGN KEY (`IdEgzaminu`) REFERENCES `Egzaminy` (`IdEgzaminu`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Wyniki_FK_2_0` FOREIGN KEY (`IdKandydata`) REFERENCES `Kandydaci` (`IdKandydata`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
