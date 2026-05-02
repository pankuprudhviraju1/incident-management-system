import time

debounce_map = {}

def should_create_incident(component_id):
    now = time.time()

    if component_id not in debounce_map:
        debounce_map[component_id] = now
        return True

    if now - debounce_map[component_id] > 10:
        debounce_map[component_id] = now
        return True

    return False