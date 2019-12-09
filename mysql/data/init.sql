
CREATE TABLE `Map` (
  `ID` int(11) DEFAULT NULL,
  `Group` varchar(50) DEFAULT NULL,
  `Location` varchar(50) DEFAULT NULL,
  `Geography` varchar(50) DEFAULT NULL,
  `Seaside` int(11) DEFAULT NULL,
  `Resource Cards` int(11) DEFAULT NULL,
  `Military Cards` int(11) DEFAULT NULL,
  `Action Cards` int(11) DEFAULT NULL,
  `Defense` int(11) DEFAULT NULL,
  `Color` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


LOAD DATA INFILE '/docker-entrypoint-initdb.d/map.csv'
INTO TABLE Map
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
