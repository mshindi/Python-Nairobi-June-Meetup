import peewee as pw
from app.db import db


class BaseModel(pw.Model):
    class Meta:
        database = db


class Notification(BaseModel):
    receiver = pw.CharField(unique=True, null=False)
    message = pw.CharField(null=False)
