
from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
from datetime import datetime, timezone
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator






class Skill(Model):
    id =  fields.IntField(pk = True, Index = True)
    name = fields.CharField(max_length = 100, null =False, default ="Unspecified")


    
    

Skill_pydantic = pydantic_model_creator(Skill, name = "Skill")
Skill_pydantic_all = pydantic_model_creator(Skill, name = "SkillAll")
    
    
    
    
    