import redis
import json
import os
from functools import wraps
from hashlib import sha256

from settings import settings

class RedisCache:
    def __init__(self):
        self.redis_host = settings.REDIS_HOST
        self.redis_port = settings.REDIS_PORT
        self.redis_client = redis.Redis(host=self.redis_host, port=self.redis_port, db=0, decode_responses=True)

    def _generate_key(self, func_name: str, *args, **kwargs):
        key_data = f"{func_name}:{args}:{kwargs}"
        return sha256(key_data.encode()).hexdigest()

    def get(self, key: str):
        value = self.redis_client.get(key)
        if value:
            return json.loads(value)
        return None

    def set(self, key: str, value: dict, ttl: int = 60):
        self.redis_client.set(key, json.dumps(value), ex=ttl)

    def delete(self, key: str):
        self.redis_client.delete(key)
        

def unvalidate_cache(key : str):
    cache_instance = RedisCache()
    cache_instance.delete(key)


def cache(ttl: int = 60):
    cache_instance = RedisCache()
    
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = cache_instance._generate_key(func.__name__, *args, **kwargs)
            cached_result = cache_instance.get(key)
            if cached_result is not None:
                print("Value from cache")
                return cached_result
            print("Nothing on the cache")
            result = await func(*args, **kwargs)
            cache_instance.set(key, result, ttl)
            return result
        
        return wrapper
    
    return decorator