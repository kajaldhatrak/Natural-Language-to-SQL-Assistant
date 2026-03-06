CREATE DATABASE company_db;

USE company_db;

CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    amount DECIMAL(10,2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO customers (name,email,city) VALUES
('Rahul Sharma','rahul@email.com','Delhi'),
('Ananya Gupta','ananya@email.com','Mumbai'),
('Arjun Mehta','arjun@email.com','Bangalore');

INSERT INTO orders (customer_id,amount,order_date) VALUES
(1,500,'2025-01-01'),
(1,1200,'2025-01-05'),
(2,800,'2025-02-01'),
(3,2000,'2025-02-10'),
(2,1500,'2025-03-01');