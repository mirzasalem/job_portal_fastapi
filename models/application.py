from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
from datetime import datetime, timezone
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator



class Application(Model):
    id = fields.IntField(pk=True, index=True)
    user = fields.ForeignKeyField("models.User", related_name="applications")
    job = fields.ForeignKeyField("models.Job", related_name="applications")
    applied_at = fields.DatetimeField(auto_now_add=True)
    status = fields.BooleanField(default=True)
    resume_url = fields.CharField(max_length=220, default="Unspecified")
    cover_letter = fields.TextField(default="Unspecified")

    class Meta:
        unique_together = ("user", "job")  # Prevent duplicate applications
        
        
        


Application_pydantic = pydantic_model_creator(Application, name = "Application", exclude = ("applied_at", "status", "user", "job"))
Application_pydantic_all = pydantic_model_creator(Application, name = "ApplicationAll")  