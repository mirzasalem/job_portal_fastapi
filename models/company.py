from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
from datetime import datetime, timezone
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator




class Company(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=100, unique=True)
    description = fields.TextField(default="Unspecified")
    website = fields.CharField(max_length=100, default="Unspecified")
    business_description = fields.TextField(null=True)
    location = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)



Company_pydantic = pydantic_model_creator(Company, name = "Company")
Company_pydantic_all = pydantic_model_creator(Company, name = "CompanyAll")  