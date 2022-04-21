from connection import db

dish = {
    'name': 'Fried Chicken',
    'price': 50
}

inserted_dish = db.dishes.insert_one(dish)
print(inserted_dish)