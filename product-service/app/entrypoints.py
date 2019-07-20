import logging
import json
import six
from nameko.web.handlers import HttpRequestHandler
from werkzeug.wrappers import Response

from app.exceptions import HttpError


class HttpEntrypoint(HttpRequestHandler):
    """Overide Http entrypoint."""

    def handle_request(self, request):
        """Create a Custom request handler."""
        try:
            self.server.context_data_from_headers(request)
            self.get_entrypoint_parameters(request)
        except Exception as exc:
            return self.response_from_exception(exc)
        return HttpRequestHandler.handle_request(self, request)

    def response_from_exception(self, exc):
        """Return a response from exception."""
        if isinstance(exc, HttpError):
            response = Response(
                json.dumps({"error": True, "errors": str(exc)}),
                status=exc.status_code,
                mimetype="application/json",
            )
            logging.error(exc)
            return response

        if isinstance(exc, Exception):
            response = Response(
                json.dumps({"error": True, "errors": str(exc)}),
                status=500,
                mimetype="application/json",
            )
            logging.error(exc)
            return response

        return HttpRequestHandler.response_from_exception(self, exc)

    @classmethod
    def response_from_result(self, result):
        """Return a response from a json result."""
        if isinstance(result, Response):
            return result

        headers = None
        if isinstance(result, tuple):
            if len(result) == 3:
                status, headers, payload = result
            else:
                status, payload = result
        else:
            payload = result
            status = 200

        if not isinstance(payload, six.string_types):
            raise TypeError(
                "Payload must be a string. Got `{!r}`".format(payload)
            )

        return Response(
            payload,
            status=status,
            headers=headers,
            mimetype="application/json",
        )


http = HttpEntrypoint.decorator
