from fastapi import APIRouter
from app.services.ingestion_service import process_signal
from app.services.rca_service import add_rca, close_incident
from app.models.db import SessionLocal
from app.models.incident import Incident
import json

router = APIRouter()

@router.get("/")
def home():
    return {"message": "IMS running"}

@router.post("/signal")
async def ingest_signal(signal: dict):
    return await process_signal(signal)


@router.post("/incident/{incident_id}/rca")
def submit_rca(incident_id: int, body: dict):
    rca_text = body.get("rca")
    return add_rca(incident_id, rca_text)


@router.post("/incident/{incident_id}/close")
def close(incident_id: int):
    return close_incident(incident_id)


@router.get("/incidents")
def get_all_incidents():
    db = SessionLocal()
    incidents = db.query(Incident).all()

    result = []
    for inc in incidents:
        result.append({
            "id": inc.id,
            "component": inc.component,
            "status": inc.status,
            "signals": json.loads(inc.signals),
            "rca": inc.rca,
            "created_at": inc.created_at,
            "resolved_at": inc.resolved_at
        })

    return result