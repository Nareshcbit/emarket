create table if not exists items(
   id INT NOT NULL AUTO_INCREMENT,
   vendor VARCHAR(100) NOT NULL,
   category VARCHAR(100) NOT NULL,
   model VARCHAR(100) NOT NULL,
   cost INT NOT NULL,
   PRIMARY KEY ( id )
);

insert into items (vendor, category, model, cost) values('Dell', 'Laptop', '5577', 999);
insert into items (vendor, category, model, cost) values('Apple', 'iphone', 'X', 1200);
insert into items (vendor, category, model, cost) values('Samsung', 'Note', '8', 720);
insert into items (vendor, category, model, cost) values('Apple', 'iPad', 'Pro', 780);