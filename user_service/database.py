from tortoise import Tortoise
from config import DATABASE_URL

async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"db1": ["models"]}
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()