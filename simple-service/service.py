import json
from nameko.rpc import rpc
from nameko.web.handlers import http
from nameko.events import EventDispatcher


class HTTPSimpleService:
    name = "http_simple_service"

    @http("GET", "/get")
    def get(self, request):
        with open('data.json', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        return json.dumps(data)

    @http("GET", "/get/<string:id>")
    def get_by_id(self, request, id):
        with open('data.json', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        return json.dumps(data.get(id))


class RpcSimpleService:
    name = "rpc_simple_service"
    dispatch = EventDispatcher()

    @rpc
    def get(self):
        with open('data.json', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        return data

    @rpc
    def get_by_id(self, id):
        with open('data.json', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        return data.get(str(id))

    @rpc
    def payload_dispatch(self, payload):
        self.dispatch("test_pub_sub", payload)
