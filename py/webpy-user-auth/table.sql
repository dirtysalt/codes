use test;
create table sessions (
  session_id char(128) UNIQUE NOT NULL,
  atime timestamp NOT NULL default current_timestamp,
  data text
);

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user varchar(80) UNIQUE NOT NULL,
  pass varchar(80) NOT NULL,
  email varchar(80) UNIQUE NOT NULL,
  privilege INT NOT NULL DEFAULT 0
);
