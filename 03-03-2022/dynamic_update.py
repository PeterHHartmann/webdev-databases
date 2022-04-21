import sqlite3
from xxlimited import new

try:
    db = sqlite3.connect('database.sqlite')
except Exception as ex:
    print(ex)

user_id = "1"
user_name = "m"
user_email = "m@m.com"

new_item = { "user_id": user_id }
set_parts = []

if user_name:
    set_parts.append("user_name=:user_name")
    new_item["user_name"] = user_name

if user_email:
    set_parts.append("user_email=:user_email")
    new_item["user_email"] = user_email

set_parts = ','.join(set_parts)

db.execute(
    f'''
    UPDATE users 
    SET {set_parts}
    WHERE user_id = :user_id;
    '''
    , new_item)
db.commit()

users = db.execute("SELECT * FROM users;").fetchall()

print(users)