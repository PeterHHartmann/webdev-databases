import sqlite3
import uuid

user_id = str(uuid.uuid4())
user_name = 'Peter'

db = sqlite3.connect('database.sqlite')
db.execute('INSERT INTO users VALUES(?, ?)', (user_id, user_name))
db.commit()

users = db.execute('SELECT * FROM users').fetchall()
print(users)

db.execute('DELETE FROM users WHERE user_name=?', (user_name,))
db.commit()

