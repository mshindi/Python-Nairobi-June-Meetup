import peewee as pw
from app.db import db


class BaseModel(pw.Model):
    class Meta:
        database = db


class User(BaseModel):
    user_name = pw.CharField(unique=True, null=False)
    password = pw.CharField(null=False)
