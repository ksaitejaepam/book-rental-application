from tortoise import Tortoise, fields
from tortoise.models import Model
from app.config import DATABASE_URL

async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["app.models"]}  # Models file
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()
