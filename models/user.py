# app/models/user.py
from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=128)
    is_active = fields.BooleanField(default=True)
    is_verified = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    
# User_pydantic = pydantic_model_creator(User, name = "User" , exclude = ("created_at", "is_verified" , "updated_at"))
# User_pydantic_all = pydantic_model_creator(User, name = "UserAll" )