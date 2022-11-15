import pandas as pd
from sqlalchemy import create_engine

conn_url = 'postgresql://postgres:123@localhost/etl_demo'
engine = create_engine(conn_url)
connection = engine.connect()

create_tables_stmt = """
CREATE TABLE users (
    id SERIAL,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE posts (
    id SERIAL,
    title VARCHAR(50) NOT NULL,
    body TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

# connection.execute(create_tables_stmt)

insert_stmt = """
INSERT INTO users (id, name, email, password) VALUES
    (1, 'John', 'john@example.com', '123'),
    (2, 'Jane', 'jane@example.com', '456'),
    (3, 'Jack', 'jack@example.com', '789');

INSERT INTO posts (id, title, body, user_id) VALUES
    (1, 'Post 1', 'This is post 1', 1),
    (2, 'Post 2', 'This is post 2', 1),
    (3, 'Post 3', 'This is post 3', 2),
    (4, 'Post 4', 'This is post 4', 3);
"""

# connection.execute(insert_stmt)

users_df = pd.read_sql('SELECT * FROM users;', engine)
print(users_df)

posts_df = pd.read_sql('SELECT * FROM posts;', engine)
print(posts_df)
