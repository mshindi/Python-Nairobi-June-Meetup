import json
from playhouse.shortcuts import model_to_dict
from app.models import Product
from app.exceptions import BadRequest, Unauthorized
from app.db import db


def get(pk=None):
    if pk:
        product = model_to_dict(
            Product.select().where(Product.id == pk).get())
        return json.dumps(product)

    prodcuts = list(Product.select())
    return json.dumps([model_to_dict(item.get()) for item in prodcuts])


def add(request):
    data = json.loads(request.data)
    product_name = data.get("product_name")
    stock = data.get("stock")
    if product_name is None or stock is None:
        raise BadRequest("Product Name and Stock are required")
    product = Product.create(product_name=product_name, stock=stock)
    return 200, json.dumps(model_to_dict(product))


def edit_stock(request, pk):
    data = json.loads(request.data)
    stock = data.get("stock")
    if stock is None:
        raise BadRequest("Stock is required")

    product = Product.update(stock=stock).where(Product.id == pk).execute()

    return 200, json.dumps(model_to_dict(Product.select().where(Product.id == pk).get()))

def delete(request, pk):
    if pk is None:
        raise BadRequest("Product id is required")
    product = Product.delete().where(Product.id == pk).execute()

    return 200, json.dumps({"Product Deleted": True})


def update_stock(stock, pk):
    product = Product.update(stock=stock).where(Product.id == pk).execute()
    print("Stock updated")
    return 200


def create_tables():
    with db:
        db.create_tables([Product])
