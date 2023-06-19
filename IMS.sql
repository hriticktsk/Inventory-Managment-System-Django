create database proinv;
use proinv;
create table crud (id int auto_increment, product varchar(20), customer varchar(20), retailer varchar(20), price varchar(20), address varchar(50), date varchar(20), amount double, totalchange double,primary key(id) );
desc crud;
select * from crud;

create table user (fname varchar(20), lname varchar(20), username varchar(20), email varchar(20), password varchar(20));
desc user;
select * from user;

