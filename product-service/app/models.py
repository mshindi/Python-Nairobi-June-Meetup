import peewee as pw
from app.db import db


class BaseModel(pw.Model):
    class Meta:
        database = db


class Product(BaseModel):
    product_name = pw.CharField(unique=True, null=False)
    stock = pw.FloatField(null=False)
