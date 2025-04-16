from fastapi import FastAPI
from app.database import init_db, close_db
from app.routers import router
from app.exceptions import register_exception_handlers

app = FastAPI(title="User Service API")

app.include_router(router, prefix="/users", tags=["Users related endpoints"])

register_exception_handlers(app)

@app.on_event("startup")
async def startup():
    await init_db()


@app.on_event("shutdown")
async def shutdown():
    await close_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
