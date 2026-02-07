# app/database.py
from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",  # Change to PostgreSQL if needed
        modules={"models": ["app.models"]},
    )
    await Tortoise.generate_schemas()
