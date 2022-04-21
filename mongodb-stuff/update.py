from connection import db

search_query = {
    
}
update_with = {
    '$set': {
        'euro': 6
    }
}

db.dishes.update_many(search_query, update_with)