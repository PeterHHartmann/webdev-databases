import redis

try:
  # decode_responses=True converts bytes to string
  r = redis.Redis(
      host='127.0.0.1',
      port=6379, 
      password='',
      decode_responses=True)

  r.set('foo', "1")
  value = r.get('foo')
  print(type(value))

  r.hset("user:1000", mapping={"name":"a", "age":10})
  print(r.hkeys("user:1000")) # ['name', 'age']
  print(r.hget("user:1000", "name")) # a
  print(r.hgetall("user:1000")) # {'name': 'a', 'age': '10'}
  r.hdel("user:1000", "age")
  print(r.hgetall("user:1000")) # {'name': 'a'}
except Exception as ex:
  print(ex)

