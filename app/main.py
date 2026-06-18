from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="Financial Event Service",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(
    health.router,
    prefix="/health",
    tags=["health"],
)