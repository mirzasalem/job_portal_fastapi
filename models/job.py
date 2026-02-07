from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
from datetime import datetime, timezone
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator




    
class Job(Model):
    id = fields.IntField(pk=True, index=True)
    title = fields.CharField(max_length=100)
    description = fields.TextField(default="Unspecified")
    company_name = fields.CharField(max_length=100)
    location = fields.CharField(max_length=100, default="Unspecified")
    employment_type = fields.CharField(max_length=50, null=True)  # full-time/part-time/remote
    experience_level = fields.CharField(max_length=50, null=True) 
    salary_min = fields.FloatField(null=True)
    salary_max = fields.FloatField(null=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    owner = fields.ForeignKeyField("models.User", related_name="user")
    applications = fields.ReverseRelation["Application"]

    




    
# class AuditModel(Model):
#     created_at = fields.DatetimeField(auto_now_add=True)
#     updated_at = fields.DatetimeField(auto_now=True)
#     deleted_at = fields.DatetimeField(null=True)
    
#     class Meta:
#         abstract = True
        





Job_pydantic = pydantic_model_creator(Job, name = "Job", exclude = ("created_at", "is_active", "owner", "applications "))
Job_pydantic_all = pydantic_model_creator(Job, name = "JobAll")

    
    
    
# user_pydantic = pydantic_model_creator(User, name = 'User', exclude = ("is_verified" ,))
# user_pydanticIn = pydantic_model_creator(User, name = "UserIn", exclude_readonly = True, exclude = ("is_verified" ,"join_date"))
# user_pydanticOut = pydantic_model_creator(User, name = "UserOut",exclude = ("password", ))


# business_pydantic = pydantic_model_creator(Business, name = "Business")
# business_pydanticIn = pydantic_model_creator(Business, name = "BusinessIn", exclude_readonly=True, exclude= ("id", "logo"))
# # business_pydanticOut = pydantic_model_creator(Business, name = "BusinessOut")



# Product_pydanticIn = pydantic_model_creator(Product, name = "ProductIn", exclude= ("percentage_discount", "id", "product_image", "date_published"))