-- States table
-- creates the database hbtn_0d_usa in the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create a table named states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
  id INT AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  CONSTRAINT PK_states PRIMARY KEY (id)
);
