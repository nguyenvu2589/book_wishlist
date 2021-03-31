
CREATE TABLE wl_user (
  user_id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password TEXT,
  created timestamp without time zone DEFAULT now(),
  last_modified timestamp without time zone DEFAULT now()
);


CREATE TABLE book (
  isbn TEXT PRIMARY KEY,
  title TEXT,
  author TEXT,
  date_of_publication DATE,
  created timestamp without time zone DEFAULT now(),
  last_modified timestamp without time zone DEFAULT now()
);


CREATE TABLE wish_list (
  id INT PRIMARY KEY,
  user_id INT REFERENCES wl_user (user_id),
  book_id TEXT REFERENCES book (isbn),
  created timestamp without time zone DEFAULT now(),
  last_modified timestamp without time zone DEFAULT now()
);


INSERT INTO wl_user (first_name, last_name, email) VALUES
('John', 'Doe', 'johndoe@gmail.com');


INSERT INTO book (isbn, title, author, date_of_publication) VALUES
('123-123', 'Shuggie Bain','Douglas Stuart', '2021-01-01' );

