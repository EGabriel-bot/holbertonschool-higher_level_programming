-- States table
-- creates the database hbtn_0d_usa and the table states in the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states(
  id INT AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL
  CONTRAINT PK_states PRIMARY KEY (id)
);
