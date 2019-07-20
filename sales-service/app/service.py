import json
from app.entrypoints import http
from nameko.rpc import rpc
from nameko.events import event_handler, EventDispatcher
from app import views

class HTTPSalesService:
    name = "http_sale_service"
    dispatch = EventDispatcher()

    @http("GET", "/sale/init-db")
    def init_db(self, request):
        views.create_tables()
        return json.dumps({"success": True})

    @http("GET", "/sale")
    def get_sale(self, request):
        return views.get()

    @http("GET", "/sale/<pk>")
    def get_by_id(self, request, pk):
        return views.get(pk)

    @http("POST", "/sale")
    def add_sale(self, request):
        return views.add(request, self.dispatch)

    @http("DELETE", "/sale/<pk>")
    def register(self, request, pk):
        return views.delete(request, pk)
