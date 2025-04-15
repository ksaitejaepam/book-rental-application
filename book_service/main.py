from fastapi import FastAPI
from routes import router
from database import init_db, close_db

app = FastAPI(title="Book Service")

# Include Routes
app.include_router(router, prefix="/books", tags=["Books"])

@app.on_event("startup")
async def startup():
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)