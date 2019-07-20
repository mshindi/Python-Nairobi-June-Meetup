import json
from app.entrypoints import http
from nameko.rpc import rpc
from nameko.events import event_handler
from app import views


class HTTPProductService:
    name = "http_product_service"

    @http("GET", "/product/init-db")
    def init_db(self, request):
        views.create_tables()
        return json.dumps({"success": True})

    @http("GET", "/product")
    def get_product(self, request):
        return views.get()

    @http("GET", "/product/<pk>")
    def get_by_id(self, request, pk):
        return views.get(pk)

    @http("POST", "/product")
    def add_product(self, request):
        return views.add(request)

    @http("PUT", "/product/<pk>")
    def edit_stock(self, request, pk):
        return views.edit_stock(request, pk)

    @http("DELETE", "/product/<pk>")
    def register(self, request, pk):
        return views.delete(request, pk)

    @event_handler("http_sales_service", "update_stock")
    def update_stock(self, payload):
        data = json.loads(payload)
        views.edit_stock(data.get("stock"), data.get("product_id"))

    @rpc
    def rpc_get_product(self, pk):
        return views.get(pk)
