import redis
import os


def get_redis_client() -> redis.Redis:
    """
    Инициализация Redis
    """
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        decode_responses=True
    )
