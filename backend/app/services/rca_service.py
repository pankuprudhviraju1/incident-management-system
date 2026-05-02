from app.models.db import SessionLocal
from app.models.incident import Incident
import datetime

def add_rca(incident_id, rca_text):
    db = SessionLocal()

    incident = db.query(Incident).filter(Incident.id == incident_id).first()

    if not incident:
        return {"error": "Incident not found"}

    incident.rca = rca_text
    incident.status = "RESOLVED"

    db.commit()

    return {"message": "RCA added successfully"}

def close_incident(incident_id):
    db = SessionLocal()

    incident = db.query(Incident).filter(Incident.id == incident_id).first()

    if not incident:
        return {"error": "Incident not found"}

    if not incident.rca:
        return {"error": "RCA required before closing"}

    incident.status = "CLOSED"
    incident.resolved_at = str(datetime.datetime.utcnow())

    db.commit()

    # MTTR calculation (simple)
    mttr = f"{incident.resolved_at} - {incident.created_at}"

    return {
        "message": "Incident closed",
        "MTTR": mttr
    }