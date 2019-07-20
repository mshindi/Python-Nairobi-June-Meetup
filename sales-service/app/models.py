import peewee as pw
from app.db import db


class BaseModel(pw.Model):
    class Meta:
        database = db


class Sale(BaseModel):
    quantity = pw.FloatField(null=False)
    product_id = pw.IntField(null=False)
    user_id = pw.IntField(null=False)
