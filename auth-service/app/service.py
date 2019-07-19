import json
from app.entrypoints import http
from app import views


class HTTPAuthService:
    name = "http_auth_service"

    @http("GET", "/auth/init-db")
    def init_db(self, request):
        views.create_tables()
        return json.dumps({"success": True})

    @http("POST", "/auth/login")
    def login(self, request):
        return views.login(request)

    @http("POST", "/auth/register")
    def register(self, request):
        return views.register(request)
