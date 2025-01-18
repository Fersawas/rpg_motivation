import redis

r = redis.Redis(host='172.23.94.236', port=6379, db=0)

try:
    print(r.ping())  # должно вернуть True
except redis.exceptions.ConnectionError as e:
    print(f"Ошибка подключения: {e}")
