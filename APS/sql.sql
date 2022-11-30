create database aps;
use aps;
drop database aps;

create table cargos(
CD_cargo int(20) PRIMARY KEY,
Cargo_desc varchar(40),
Nivel_poder varchar(20)
);

create table funcionarios(
CD_func int(20) PRIMARY KEY auto_increment,
Nome varchar(20),
Usuario varchar(40) UNIQUE,
Senha varchar(40) UNIQUE,
CD_cargo int(20) NOT NULL,
FOREIGN KEY (CD_cargo) REFERENCES cargos(CD_cargo)
);

create table docs(
CD_doc int(20) PRIMARY KEY auto_increment,
CD_dono int(20) ,
Nome varchar(40),
Nivel int(20),
Texto varchar(2000),
FOREIGN KEY (CD_dono) REFERENCES funcionarios(CD_func),
FOREIGN KEY (Nivel) REFERENCES cargos(CD_cargo)
);

Select*from cargos;
Select*from funcionarios;
Select*from docs;

insert into cargos (CD_cargo,Cargo_desc,Nivel_poder) VALUES (1,"Presidente","Forte");
insert into cargos (CD_cargo,Cargo_desc,Nivel_poder) VALUES (2,"Vice-presidente","Moderado");
insert into cargos (CD_cargo,Cargo_desc,Nivel_poder) VALUES (3,"Gerente","Mediano");
insert into cargos (CD_cargo,Cargo_desc,Nivel_poder) VALUES (4,"Analista","Regular");
insert into cargos (CD_cargo,Cargo_desc,Nivel_poder) VALUES (10,"Sistema","Nenhum");
insert into funcionarios (Nome,usuario,Senha,CD_cargo) VALUES ("Antony","Tony","pass123",1);
insert into funcionarios (Nome,usuario,Senha,CD_cargo) VALUES ("Thiago","Capivara","Capivara123",2);
insert into funcionarios (Nome,usuario,Senha,CD_cargo) VALUES ("Diego","Deigo","lol123",3);
insert into funcionarios (Nome,usuario,Senha,CD_cargo) VALUES ("Kaique","Gobitta","miriam123",4);
insert into funcionarios (Nome,usuario,Senha,CD_cargo) VALUES ("a","a","a",1);
insert into funcionarios (CD_func,Nome,usuario,Senha,CD_cargo) VALUES (10,"CENTRAL","&","&",10);
insert into docs (CD_dono,Nome,Nivel,Texto) VALUES (10,"Mata Atlântica",10,
"A Mata Atlântica é um bioma composto por um conjunto de florestas e ecossistemas que corresponde a 15% do território brasileiro.
Desde 1500, essa área vem sofrendo com o desmatamento, as queimadas e a degradação do ambiente.
É por isso que, atualmente, a vegetação corresponde a apenas 7% da mata original, com árvores de médio e grande porte, constituindo uma floresta densa e fechada.");

insert into docs (CD_dono,Nome,Nivel,Texto) VALUES (10,"Floresta Amazônica",10,
"A floresta amazônica é considerada a maior floresta tropical do mundo e concentra enorme biodiversidade. Além disso, ela faz parte do bioma Amazônia, o maior dos seis biomas brasileiros.
Ela corresponde a 53% das florestas tropicais ainda existentes. Por isso, a sua conservação é debatida em âmbito internacional por sua dimensão e importância ecológica.");



SELECT d.Nome,d.CD_dono FROM  funcionarios f
INNER JOIN docs d ON f.CD_func = d.CD_dono where d.CD_dono=5;
DELETE FROM funcionarios WHERE CD_func=8;
SELECT Usuario,Senha FROM funcionarios where Nome='Kaique';

