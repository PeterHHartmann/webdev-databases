from connection import db

print(db)

dishes_cursor = db.dishes.find()
dishes = [dish for dish in dishes_cursor]
print('This is the list', dishes)