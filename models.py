from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
from datetime import datetime
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    id = fields.IntField(pk=True, index=False)
    username = fields.CharField(max_length=100, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=128)
    is_verified = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(default=datetime.utcnow)
    updated_at = fields.DatetimeField(default=datetime.utcnow)
    is_active = fields.BooleanField(default=True)
    role = fields.CharField(max_length=50)  # employee / job_seeker / employer

    jobs = fields.ReverseRelation["Job"]       # One-to-many: User → Job
    applications = fields.ReverseRelation["Application"]  # User → Application

    
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
    created_at = fields.DatetimeField(default=datetime.utcnow)

    owner = fields.ForeignKeyField("models.User", related_name="user")
    applications = fields.ReverseRelation["Application"]

    
class Application(Model):
    id = fields.IntField(pk=True, index=True)
    user = fields.ForeignKeyField("models.User", related_name="applications")
    job = fields.ForeignKeyField("models.Job", related_name="applications")
    applied_at = fields.DatetimeField(default=datetime.utcnow)
    status = fields.BooleanField(default=True)
    resume_url = fields.CharField(max_length=220, default="Unspecified")
    cover_letter = fields.CharField(max_length=220, default="Unspecified")

    class Meta:
        unique_together = ("user", "job")  # Prevent duplicate applications

class Skill(Model):
    id =  fields.IntField(pk = True, Index = True)
    name = fields.CharField(max_length = 100, null =False, default ="Unspecified")


    
class Company(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=100, unique=True)
    description = fields.TextField(default="Unspecified")
    website = fields.CharField(max_length=100, default="Unspecified")
    business_description = fields.TextField(null=True)
    location = fields.TextField(null=True)
    created_at = fields.DatetimeField(default=datetime.utcnow)

    
class AuditModel(Model):
    created_at = fields.DatetimeField(default=datetime.utcnow)
    updated_at = fields.DatetimeField(default=datetime.utcnow)
    deleted_at = fields.DatetimeField(null=True)
    
    class Meta:
        abstract = True

    
Application_pydantic = pydantic_model_creator(Application, name = "Application", exclude = ("created_at", "is_active", "user", "job", "status"))
Application_pydantic_all = pydantic_model_creator(Application, name = "ApplicationAll")  
    
    
    
    
    
    
    
    
    
    
# user_pydantic = pydantic_model_creator(User, name = 'User', exclude = ("is_verified" ,))
# user_pydanticIn = pydantic_model_creator(User, name = "UserIn", exclude_readonly = True, exclude = ("is_verified" ,"join_date"))
# user_pydanticOut = pydantic_model_creator(User, name = "UserOut",exclude = ("password", ))


# business_pydantic = pydantic_model_creator(Business, name = "Business")
# business_pydanticIn = pydantic_model_creator(Business, name = "BusinessIn", exclude_readonly=True, exclude= ("id", "logo"))
# # business_pydanticOut = pydantic_model_creator(Business, name = "BusinessOut")

User_pydantic = pydantic_model_creator(User, name = "User" , exclude = ("created_at", "is_verified" , "updated_at"))
User_pydantic_all = pydantic_model_creator(User, name = "UserAll" )


Job_pydantic = pydantic_model_creator(Job, name = "Job", exclude = ("created_at", "is_active", "owner", "applications "))
Job_pydantic_all = pydantic_model_creator(Job, name = "JobAll")

# Product_pydanticIn = pydantic_model_creator(Product, name = "ProductIn", exclude= ("percentage_discount", "id", "product_image", "date_published"))