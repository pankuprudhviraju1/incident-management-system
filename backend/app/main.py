from fastapi import FastAPI
from app.api.routes import router
from app.models.db import engine
from app.models import incident  # important: registers the model
from app.models.db import Base

Base.metadata.create_all(bind=engine)



app = FastAPI()

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}