import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

async def process_signal(signal):
    r.lpush("signal_queue", json.dumps(signal))
    return {"message": "Signal queued for processing"}