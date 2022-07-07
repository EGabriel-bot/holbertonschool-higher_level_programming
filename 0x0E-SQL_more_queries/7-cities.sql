-- Cities table
-- script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates table cities in the hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
  id INT AUTO_INCREMENT,
  state_id INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT FK_states FOREIGN KEY (state_id) 
  REFERENCES cities (id)
);
