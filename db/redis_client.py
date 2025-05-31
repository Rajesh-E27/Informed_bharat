import os
import redis

def get_redis_connection():
    redis_url = os.getenv("REDIS_URL")  # Get Redis URL from env variable
    if not redis_url:
        # Optionally, you can set a default local Redis URL here for dev
        redis_url = "redis://localhost:6379"
    return redis.from_url(redis_url)
