-- creates a table second_table in the database hbtn_0c_0
-- second_table description: id INT, name VARCHAR(256), score INT
CREATE TABLE IF NOT EXISTS second_table(
  id INT,
  name VARCHAR(256),
  score INT
);

-- Insert values to second table
INSERT INTO second_table (
  id,
  name,
  score
)
VALUES
(
  1,"John",10
),
(
  2,"Alex",3
),
(
  3,"Bob",14
),
(
  4,"George",8
);