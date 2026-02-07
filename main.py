from fastapi import FastAPI, HTTPException
from app.models.user import User
from tortoise.contrib.fastapi import register_tortoise
from pydantic import BaseModel
from fastapi import Depends
from tortoise.contrib.pydantic import pydantic_model_creator

# Static file config setup
app = FastAPI()

# Generate Pydantic models from Tortoise models BEFORE using them in routes
User_pydantic = pydantic_model_creator(User, name="User", exclude_readonly=True)
User_pydantic_out = pydantic_model_creator(User, name="UserOut", exclude=["password_hash"])
User_pydantic_all = pydantic_model_creator(User, name="UserList")

# Register Tortoise
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.user", "app.models.job", "app.models.application"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/users")
async def get_user():
    response = await User_pydantic_all.from_queryset(User.all())
    return {"status": "ok", "data": response}

@app.post("/users")
async def create_user(user: User_pydantic):
    user_obj = await User.create(**user.dict(exclude_unset=True))
    user_obj_pydantic = await User_pydantic_out.from_tortoise_orm(user_obj)
    return {"status": "ok", "data": user_obj_pydantic}