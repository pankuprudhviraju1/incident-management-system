from sqlalchemy import Column, Integer, String, Text
from app.models.db import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    component = Column(String, index=True)
    status = Column(String)              # OPEN / INVESTIGATING / RESOLVED / CLOSED
    signals = Column(Text)               # JSON string of signals
    rca = Column(Text, nullable=True)    # Root Cause Analysis
    created_at = Column(String)
    resolved_at = Column(String, nullable=True)