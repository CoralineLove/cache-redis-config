import redis
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define Redis connection settings
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)

# Initialize Redis connection
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

# Define cache expiration time in seconds
CACHE_EXPIRATION = int(os.getenv('CACHE_EXPIRATION', 60))  # 1 minute default

# Use Redis as a cache backend for storing application data
class CacheBackend:
    def get(self, key):
        return redis_client.get(key)

    def set(self, key, value, expiration=None):
        if expiration is None:
            expiration = CACHE_EXPIRATION
        redis_client.setex(key, expiration, value)

    def delete(self, key):
        redis_client.delete(key)

# Initialize the cache backend
cache = CacheBackend()

# Example usage:
if __name__ == '__main__':
    cache.set('my_key', 'my_value')
    print(cache.get('my_key'))  # prints: my_value
    cache.delete('my_key')