import sqlite3
conn = sqlite3.connect('test.db')
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name text, email text)")
sql_command="""INSERT INTO users VALUES (1, 'John', '<EMAIL>')"""
conn.execute(sql_command)
conn.execute("INSERT INTO users VALUES (2, 'Doe', '<EMAIL>')")
value=conn.cursor()
value.execute("SELECT * FROM users")
for row in value:
    print(row)
conn.commit()
conn.close()
