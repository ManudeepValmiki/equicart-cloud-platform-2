from fastapi import FastAPI

app = FastAPI(
    title="EquiCart API",
    description="Cloud Native Smart Retail Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "EquiCart FastAPI Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }