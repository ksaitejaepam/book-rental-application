from fastapi import FastAPI

from app.exceptions import register_exception_handlers
from app.routers import router
from app.database import init_db, close_db

app = FastAPI(title="Book Service")

# Include Routes
app.include_router(router, prefix="/books", tags=["Books"])

register_exception_handlers(app)

@app.on_event("startup")
async def startup():
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)