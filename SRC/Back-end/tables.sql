CREATE DATABASE clothstore;
use clothstore;
CREATE TABLE cloth(
    S_no int(11),
	HSN_code int(11) primary key,
	cloth varchar(20),
	brand varchar(20),
	quantity int(11),
	cost_peritem int(11)
);
CREATE TABLE purchase(
	S_no int(11),
	HSN_code int(11) primary key,
	Item_name varchar(15) NOT NULL,
	Company varchar(10),
	Quantity varchar(30),
	costprice_peritem varchar(10),
	Purchase_Date date
);


CREATE TABLE sale (
	S_no int(11),
	HSN_code int(11) primary key, Item_name varchar(15) NOT NULL,
	Quantity varchar(30),Netcost_peritem varchar(10),Total_amount varchar(10),Sale_Date date 
);


CREATE TABLE rents_and_expenditure (
	Sno varchar(4),
	Reason_no varchar(9) primary key,
	reason varchar(50),
	floor_no varchar(4),
	amount int(11),
	Date date,
	Paid varchar(1)
);

