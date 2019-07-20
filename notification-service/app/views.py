import json
import requests
from app.models import Notification
from app.db import db


def push_notification(payload):
    data = json.loads(payload)
    print(data)
    requests.post(
        "https://webhook.site/a1b56d13-8f3d-4019-95c5-03ea5760f66e", data
    )


def create_tables():
    with db:
        db.create_tables([Notification])
