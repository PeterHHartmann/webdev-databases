import sqlite3


user = {
    'user_name': 'Peter' 
}

try:
    db = sqlite3.connect('database.sqlite')
    counter = db.execute('DELETE FROM users WHERE user_name=:user_name', user).rowcount
    db.commit()

    if not counter: print('User not found')

    print(f'Users deleted: {counter}')

except Exception as ex:
    print(ex)

finally:
    db.close()