use cabbooking;

-- trigger1 
DROP TRIGGER IF EXISTS `cabbooking`.`customer_BEFORE_INSERT`;
DELIMITER $$
USE `cabbooking`$$
CREATE DEFINER = CURRENT_USER TRIGGER `cabbooking`.`customer_BEFORE_INSERT` BEFORE INSERT ON `customer` FOR EACH ROW
BEGIN
	IF NEW.CUST_RATING < 0 THEN SET NEW.CUST_RATING = 0;
    END IF;
END$$
DELIMITER ;


-- To check the trigger
select * from CUSTOMER;
INSERT INTO `cabbooking`.`CUSTOMER` (`CUSTOMER_ID`, `FIRST_NAME`, `LAST_NAME`, `CONTACT_NO`, `CUST_PASSWORD`, `WALLET`, `LOCATION_X`, `LOCATION_Y`, `CUST_RATING`, `ADDRESS`, `EMERGENCY_CONTACT`) VALUES ('102', 'vee', 'bee', '9087579331', 'haksjds', '90', '9023', '123', '-20', 'sdfkdsfl', '9089273732');


-- trigger 2 : someone can only increase the trip count by 1 of any driver 
DROP TRIGGER IF EXISTS `cabbooking`.`driver_BEFORE_UPDATE`;

DELIMITER $$
USE `cabbooking`$$
CREATE DEFINER = CURRENT_USER TRIGGER `cabbooking`.`driver_BEFORE_UPDATE` BEFORE UPDATE ON `driver` FOR EACH ROW
BEGIN
	IF NEW.TRIP_COUNT != OLD.TRIP_COUNT + 1 THEN SET NEW.TRIP_COUNT = OLD.TRIP_COUNT;
    END IF;
END$$
DELIMITER ;

SELECT * FROM DRIVER;
UPDATE `cabbooking`.`DRIVER` SET `TRIP_COUNT` = '9514' WHERE (`DRIVER_ID` = '1');


-- OLAP Queries 



