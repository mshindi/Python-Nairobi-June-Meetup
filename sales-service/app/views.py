import json
from playhouse.shortcuts import model_to_dict
from app.models import Sale
from app.exceptions import BadRequest, Unauthorized
from app.db import db


def get(pk=None):
    if pk:
        Sale = model_to_dict(
            Sale.select().where(Sale.id == pk).get())
        return json.dumps(Sale)

    prodcuts = list(Sale.select())
    return json.dumps([model_to_dict(item.get()) for item in prodcuts])


def add(request, dispatcher):
    data = json.loads(request.data)
    user_id = data.get("user_id")
    quantity = data.get("quantity")
    product_id = data.get("product_id")
    if user_id is None or quantity is None or product_id is None:
        raise BadRequest("Sale Id, User  Id and are Quantity required")

    # do rpc request to get stock from product service
    Sale = Sale.create(Sale_name=Sale_name, stock=stock)
    payload  = {
        "stock": (stock - quantity),
        "product_id": product_id
        }
    dispatcher("update_stock", payload)
    return 200, json.dumps(model_to_dict(Sale))


def edit_stock(request, pk):
    data = json.loads(request.data)
    stock = data.get("stock")
    if stock is None:
        raise BadRequest("Stock is required")

    Sale = Sale.update(stock=stock).where(Sale.id == pk).execute()

    return 200, json.dumps(model_to_dict(Sale.select().where(Sale.id == pk).get()))

def delete(request, pk):
    if pk is None:
        raise BadRequest("Sale id is required")
    Sale = Sale.delete().where(Sale.id == pk).execute()

    return 200, json.dumps({"Sale Deleted": True})


def update_stock(stock, pk):
    Sale = Sale.update(stock=stock).where(Sale.id == pk).execute()
    print("Stock updated")
    return 200


def create_tables():
    with db:
        db.create_tables([Sale])
