import json
from app.models import User
from app.exceptions import BadRequest, Unauthorized
from app.db import db


def login(request):
    data = json.loads(request.data)
    user_name = data.get("user_name")
    password = data.get("password")
    if password is None or user_name is None:
        raise BadRequest("User Name and Password are required")
    user = User.get(User.user_name == user_name)
    if user is None or user.password != password:
        raise Unauthorized("Invalid user name or password")
    return 200, json.dumps({"success": True})


def register(request):
    data = json.loads(request.data)
    user_name = data.get("user_name")
    password = data.get("password")
    if password is None or user_name is None:
        raise BadRequest("User Name and Password are required")
    user = User.create(password=password, user_name=user_name)
    return 201, json.dumps({"user_name": user.user_name})


def create_tables():
    with db:
        db.create_tables([User])
