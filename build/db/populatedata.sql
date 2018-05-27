create table authors_tbl(
   author_id INT NOT NULL AUTO_INCREMENT,
   author_firstname VARCHAR(100) NOT NULL,
   author_lastname VARCHAR(100) NOT NULL,
   PRIMARY KEY ( author_id )
);

insert into authors_tbl (author_firstname, author_lastname) values('naresh', 'madiraju');
insert into authors_tbl (author_firstname, author_lastname) values('ratan', 'tata');
insert into authors_tbl (author_firstname, author_lastname) values('steve', 'jobs');
insert into authors_tbl (author_firstname, author_lastname) values('warren', 'buffet');