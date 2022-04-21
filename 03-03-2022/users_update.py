import sqlite3

user = {
    'user_id': '20d38d0f-bcf0-4d56-95a5-b127608ca5b3',
    'new_user_name': 'NEW USER NAME'
}

try:
    db = sqlite3.connect('database.sqlite')
    counter = db.execute('''
        UPDATE users
        SET user_name = :new_user_name
        WHERE user_id = :user_id
    ''', user).rowcount
    db.commit()

    if not counter: print('User not found')

    print(f'Number of users updated: {counter}')
except Exception as ex:
    print(ex)
finally:
    db.close()
