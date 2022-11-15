import pandas as pd
from sqlalchemy import create_engine

conn_url = 'postgresql://postgres:123@localhost/uni_small'
engine = create_engine(conn_url)

df = pd.read_sql('SELECT * FROM student;', engine)

print(df)
