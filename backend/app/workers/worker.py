import redis
import json
from app.utils.debounce import should_create_incident
from app.services.incident_service import create_incident, add_signal_to_incident

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

print("🚀 Worker started...")

while True:
    data = r.brpop("signal_queue")
    signal = json.loads(data[1])

    component_id = signal.get("component")

    if should_create_incident(component_id):
        incident = create_incident(component_id, signal)
        print("🆕 New incident created:", incident)
    else:
        incident = add_signal_to_incident(component_id, signal)
        print("➕ Signal added:", incident)