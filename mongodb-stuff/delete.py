from connection import db

dish_to_delete = {
    'name': 'Fried Chicken'
}

db.dishes.delete_one(dish_to_delete)