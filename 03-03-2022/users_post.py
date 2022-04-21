import sqlite3
import uuid

user = {
    'user_id': str(uuid.uuid4()),
    'user_name': 'Peter',
    'user_email': 'test@mail.com'
}

try:
    db = sqlite3.connect('database.sqlite')

    # using dictionary and named placeholders
    db.execute('INSERT INTO users VALUES(:user_id, :user_name, :user_email)', user)

    ## using placeholders with ? - bindings
    # db.execute('INSERT INTO users VALUES(?, ?)', (user_id, user_name))
    db.commit()
except Exception as ex:
    print(ex)
    if 'user_email' in str(ex):
        print('Email already exists')

finally:
    db.close()