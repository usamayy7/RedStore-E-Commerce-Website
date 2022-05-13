CREATE DATABASE Kapre_Db;
USE Kapre_Db;
Create table Customer (
CustID int not null unique,
Fname varchar(20),
Lname varchar(20),
Gender char(20),
Username varchar(20),
passowrd varchar(20),
Email varchar(30),
Phone int(10),
Zip   int(10),
District varchar (20),
Province varchar (20),
primary key(CustID)
);

create table Category (
CatID int not null unique,
CatName varchar(10),
primary key (CatID)
);

create table Product (
ProID int not null unique,
ProPrice int(10),
ProName varchar(10),
ProModel varchar(10),
CustID int,
CatID int,
primary key (ProID),
foreign key (CustID) References Customer(CustID) 
ON UPDATE CASCADE On delete restrict,
foreign key (CatID) References Category(CatID) 
ON UPDATE CASCADE On delete restrict
);

create table Cart (
CartID int not null unique,
TotalPrice int(10),
Quantity int(10),
ProID int,
primary key (CartID),
foreign key (ProID) References Product(ProID) 
ON UPDATE CASCADE On delete restrict
);

create table Payment (
PayID int not null unique,
PayType varchar(10),
CartID int,
primary key (PayID),
foreign key (CartID) References Cart(CartID) 
ON UPDATE CASCADE On delete restrict
);

Create table Review (
ReviewID int not null unique,
ReviewText varchar(50),
CustID int,
ProID int,
primary key (reviewID),
foreign key (CustID) References Customer(CustID) 
ON UPDATE CASCADE On delete restrict,
Foreign key (ProID) References Product(ProID) 
ON UPDATE CASCADE On delete restrict
);



