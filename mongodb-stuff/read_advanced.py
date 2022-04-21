from connection import db 

aggregator_search_query = {
    'euro': {'$gt': 10}
}

dishes_cursor = db.dishes.find(aggregator_search_query)

dishes = [dish for dish in dishes_cursor]

print(dishes)
