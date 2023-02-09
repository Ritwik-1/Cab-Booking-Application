SET NAMES utf8mb4;
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS CabBooking;
CREATE SCHEMA CabBooking;
USE CabBooking;

CREATE TABLE IF NOT exists CUSTOMER (
	 CUSTOMER_ID int NOT NULL auto_increment,
	 FIRST_NAME varchar(40) NOT NULL,
     LAST_NAME varchar(40),
     CONTACT_NO bigint NOT NULL unique,
     
     CUST_PASSWORD  varchar(20) NOT NULL,
	 WALLET float,
     LOCATION_X float NOT NULL,
     LOCATION_Y float NOT NULL,
     CUST_RATING int,
	 ADDRESS varchar(200),
     EMERGENCY_CONTACT bigint,

     primary key(CUSTOMER_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT exists DRIVER (
	 DRIVER_ID int NOT NULL auto_increment,
     VEHICLE_REG_NO varchar(20),
	 FIRST_NAME varchar(40) NOT NULL,
     LAST_NAME varchar(40),
     GENDER     varchar(20),
     CONTACT_NO bigint NOT NULL unique,
     
     DRIVER_PASSWORD   varchar(20) NOT NULL,
	 DRIVER_RATING int,
     
     AVAILABILITY bool NOT NULL default TRUE,
     LICENSE_NO   varchar(20) NOT NULL unique,
     TRIP_COUNT   int default 0,
     
     LOCATION_X float NOT NULL,
     LOCATION_Y float NOT NULL,
     
	 ADDRESS varchar(200),
     primary key(DRIVER_ID),
     foreign key(VEHICLE_REG_NO) references VEHICLE(VEHICLE_REG_NO)
     
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT exists ADMIN (
	 ADMIN_ID int NOT NULL,
     ADMIN_USERNAME varchar(20),
     ADMIN_PASSWORD varchar(15),
     primary key(ADMIN_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT exists VEHICLE (
    VEHICLE_REG_NO varchar(10) NOT NULL,
    VEHICLE_NAME varchar(20) NOT NULL,
    AC bool,
    ELECTRIC_VEHICLE bool default FALSE,
    FUEL_TYPE bool default TRUE,
    POLLUTION_CERT_NO varchar(20) NOT NULL,
    VEHICLE_TYPE varchar(20) NOT NULL,
    LUGGAGE_CARRIER bool default FALSE,
    BOOT_SPACE float,
    SEATING_CAP int default 4,
    primary key(VEHICLE_REG_NO)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT exists RIDE_DETAILS(
	 DRIVER_ID int NOT NULL,
     CUSTOMER_ID int NOT NULL,
     
     SOURCE_ADDRESS varchar(50) NOT NULL,
     DESTINATION_ADDRESS varchar(50) NOT NULL,
	
     -- current Timesptamp return currnt DT
     
     -- changed  
     RIDE_START_DATE varchar(10),
	 RIDE_END_DATE  varchar(10),
     
     RIDE_START_TIME time,
     RIDE_END_TIME time,
     
     COMPLETION_STATUS bool default FALSE,
	 PAYMENT_AMOUNT float default 0,
     
     CUSTOMER_FEEDBACK varchar(500),
     DRIVER_FEEDBACK varchar(500),
     
     RATING_BY_CUST int,
     RATING_BY_DRIVER int,
     
     foreign key(DRIVER_ID) references DRIVER(DRIVER_ID),
     foreign key(CUSTOMER_ID) references CUSTOMER(CUSTOMER_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT exists DRIVER_VEHICLE(
     DRIVER_ID int NOT NULL,
     VEHICLE_REG_NO varchar(10) NOT NULL,
     foreign key(DRIVER_ID) references DRIVER(DRIVER_ID),
     foreign key(VEHICLE_REG_NO) references VEHICLE(VEHICLE_REG_NO)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT exists FEEDBACK_RIDES(
     DRIVER_ID int NOT NULL,
     CUSTOMER_ID int NOT NULL,
     ADMIN_ID int NOT NULL,
     
     foreign key(DRIVER_ID) references DRIVER(DRIVER_ID),
	 foreign key(CUSTOMER_ID) references CUSTOMER(CUSTOMER_ID),
	 foreign key(ADMIN_ID) references ADMIN(ADMIN_ID)
     
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- CREATE TABLE HATCHBACK(
-- 	VEHICLE_REG_NO varchar(10) NOT NULL,
--     VEHICLE_NAME varchar(20),
--     AC bool,
--     ELECTRIC_VEHICLE bool,
--     FUEL_TYPE varchar(10),
--     POLLUTION_CERT_NO varchar(20),
--     
--     BOOT_SPACE int
--     
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- CREATE TABLE SEDAN(
-- 	VEHICLE_REG_NO varchar(10) NOT NULL,
--     VEHICLE_NAME varchar(20),
--     AC bool,
--     ELECTRIC_VEHICLE bool,
--     FUEL_TYPE varchar(10),
--     POLLUTION_CERT_NO varchar(20),
--     
--     SEAT_NUMBER int default 4
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- CREATE TABLE SUV(
-- 	VEHICLE_REG_NO varchar(10) NOT NULL,
--     VEHICLE_NAME varchar(20),
--     AC bool,
--     ELECTRIC_VEHICLE bool,
--     FUEL_TYPE varchar(10),
--     POLLUTION_CERT_NO varchar(20),
--     
--     LUGGAGE_CARRIER bool 
--     
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;





