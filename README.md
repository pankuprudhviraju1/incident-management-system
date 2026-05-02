# 🚀 Incident Management System (IMS)

## 📌 Overview
This project is a production-style Incident Management System designed to handle high-throughput failure signals, group them into incidents, and manage lifecycle workflows with mandatory Root Cause Analysis (RCA).

---

## 🧠 Architecture

Client → FastAPI → Redis Queue → Worker → SQLite DB
↓
Debouncing Logic


---

## ⚙️ Features
- ⚡ High-throughput ingestion using Redis queue  
- 🔄 Async processing via worker system  
- 🧠 Debouncing logic (100 signals → 1 incident)  
- 📊 Incident lifecycle management  
  - OPEN → RESOLVED → CLOSED  
- 🔐 Mandatory RCA before closing  
- ⏱ MTTR calculation  
- 💾 Persistent storage (SQLite)  
- 📡 Health monitoring endpoint  

---

## 🧱 Tech Stack
- FastAPI  
- Redis  
- SQLite  
- SQLAlchemy  
- Python  

---

## ▶️ How to Run

```bash
# Clone repo
git clone <your-repo-link>
cd incident-management-system/backend

# Activate virtual env
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Redis
brew services start redis

# Run backend
uvicorn app.main:app --reload

# Run worker
python -m app.workers.worker

🧪 API Endpoints
POST /signal → Ingest signal
GET /incidents → View all incidents
POST /incident/{id}/rca → Add RCA
POST /incident/{id}/close → Close incident
GET /health → Health check

🔥 Key Design Decisions
Backpressure handling via Redis queue
Separation of concerns (API, worker, DB)
Debouncing strategy to avoid alert flooding
Transactional updates for incident lifecycle

📈 Future Improvements
Add real-time dashboard (React)
Use Kafka for higher scale
Add alerting system (email/slack)
Implement distributed tracing


---

# 🎯 Final verdict

👉 Now this = **100% submission-ready README**  
👉 Before = would hurt your impression  

---

# 🚀 Next step

Say:

👉 **“next requirements.txt”**

We’ll finish:
- dependencies file  
- GitHub push  
- final PDF submission 🚀