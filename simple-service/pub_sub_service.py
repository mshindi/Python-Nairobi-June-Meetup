from nameko.events import event_handler


class PubSubService:
    name = "pub_sub_service"

    @event_handler("rpc_simple_service", "test_pub_sub")
    def handle_event(self, payload):
        print(payload)