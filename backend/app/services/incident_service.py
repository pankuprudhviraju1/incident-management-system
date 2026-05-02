import json
from app.models.db import SessionLocal
from app.models.incident import Incident

def create_incident(component_id, signal):
    db = SessionLocal()

    incident = Incident(
        component=component_id,
        status="OPEN",
        signals=json.dumps([signal]),
        created_at=signal.get("timestamp")
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return serialize(incident)

def add_signal_to_incident(component_id, signal):
    db = SessionLocal()

    incident = db.query(Incident).filter(
        Incident.component == component_id,
        Incident.status != "CLOSED"
    ).first()

    if incident:
        signals = json.loads(incident.signals)
        signals.append(signal)
        incident.signals = json.dumps(signals)

        db.commit()
        db.refresh(incident)

        return serialize(incident)

def serialize(incident):
    return {
        "id": incident.id,
        "component": incident.component,
        "status": incident.status,
        "signals": json.loads(incident.signals),
        "rca": incident.rca,
        "created_at": incident.created_at,
        "resolved_at": incident.resolved_at
    }