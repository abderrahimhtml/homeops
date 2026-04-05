from fastapi import FastAPI
import platform, datetime

app = FastAPI(title="HomeOps API")

@app.get("/")
def root():
    return {
        "status": "ok",
        "project": "HomeOps",
        "host": platform.node(),
        "time": datetime.datetime.utcnow().isoformat()
    }

@app.get("/health")
def health():
    return {"healthy": True}
