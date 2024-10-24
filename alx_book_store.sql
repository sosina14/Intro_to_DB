USE alx_book_store;
CREATE alx_book_store IF NOT EXISTS alx_book_store;
CREATE TABLE Customers(
	customer_id INT Primary Key,
	customer_name VARCHAR(215),
	email VARCHAR(215),
	address TEXT
);
CREATE TABLE Authors(
	author_id INT Primary Key,
	author_name VARCHAR(215)
);
CREATE TABLE Books (
  book_id INT PRIMARY KEY,
  title VARCHAR(130),
  author_id INT,
  price DOUBLE,
  publication_date DATE,
  FOREIGN KEY (author_id) REFERENCES Authors (author_id)
); 
CREATE TABLE Orders(
	order_id INT Primary Key,
	customer_id INT,
	order_date DATE,
	FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
);
CREATE TABLE Order_Details(
	orderdetailid INT Primary Key,
	order_id INT,
	book_id INT,
	quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES Orders (order_id),
    FOREIGN KEY (book_id) REFERENCES books (book_id)
);
