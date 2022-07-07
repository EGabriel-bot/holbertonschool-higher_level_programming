-- Cities table
-- script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates table cities in the hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
  id INT AUTO_INCREMENT,
  state_id INT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (state_id) REFERENCES states(id)
);
