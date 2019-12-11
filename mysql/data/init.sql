
CREATE TABLE `Map` (
  `ID` int(11) DEFAULT NULL,
  `Group` varchar(50) DEFAULT NULL,
  `Location` varchar(50) DEFAULT NULL,
  `Geography` varchar(50) DEFAULT NULL,
  `Seaside` int(11) DEFAULT NULL,
  `Resource_Cards` int(11) DEFAULT NULL,
  `Military_Cards` int(11) DEFAULT NULL,
  `Action_Cards` int(11) DEFAULT NULL,
  `Defense` int(11) DEFAULT NULL,
  `Color` varchar(10) DEFAULT NULL,
  `Location1` varchar(10) DEFAULT NULL,
  `Location2` varchar(10) DEFAULT NULL,
  `Location3` varchar(10) DEFAULT NULL,
  `Occupants` int(11) DEFAULT NULL,
  `Owner` int(11) DEFAULT NULL,
  `Influence` int(11) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Users` (
  `ID` int(11) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `House` varchar(50) DEFAULT NULL,
  `Color` varchar(10) DEFAULT NULL,
  `Influence` int(11) DEFAULT NULL,
  `Dentre` int(11) DEFAULT NULL,
  `Food` int(11) DEFAULT NULL,
  `Supplies` int(11) DEFAULT NULL



) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOAD DATA INFILE '/docker-entrypoint-initdb.d/map.csv'
INTO TABLE Map
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/docker-entrypoint-initdb.d/users.csv'
INTO TABLE Users
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
