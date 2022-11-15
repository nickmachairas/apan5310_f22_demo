import psycopg2

# Connect to an existing database
conn = psycopg2.connect(
    "host=localhost dbname=uni_small user=postgres password=123")

# Open a cursor to perform database operations
cur = conn.cursor()

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM student;")
print(cur.fetchall())

# Close communication with the database
cur.close()
conn.close()
