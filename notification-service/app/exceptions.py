"""Represent possible http error codes."""


class HttpError(Exception):
    """BAD_REQUEST."""

    error_code = "BAD_REQUEST"
    status_code = 400


class BadRequest(HttpError):
    """BAD_REQUEST."""

    error_code = "BAD_REQUEST"
    status_code = 400


class NotFound(HttpError):
    """NOT_FOUND."""

    error_code = "NOT_FOUND"
    status_code = 404


class DuplicateRecord(HttpError):
    """DUPLICATE_ENTRY."""

    error_code = "DUPLICATE_ENTRY"
    status_code = 409


class DatabaseError(HttpError):
    """DATABASE ERROR."""

    error_code = "DATABASE ERROR"
    status_code = 500


class ValidationFailed(HttpError):
    """VALIDATION_FAILED."""

    error_code = "VALIDATION_FAILED"
    status_code = 422


class PreconditionFailed(HttpError):
    """PRECONDITION_FAILED."""

    error_code = "PRECONDITION_FAILED"
    status_code = 412


class Forbidden(HttpError):
    """Forbidden."""

    error_code = "Forbidden"
    status_code = 403


class RemoteError(HttpError):
    """REMOTE_ERROR."""

    error_code = "REMOTE_ERROR"
    status_code = 502


class Unauthorized(HttpError):
    """Unauthorized."""

    error_code = "Unauthorized"
    status_code = 401


class Conflict(HttpError):
    """Conflict."""

    error_code = "Conflict"
    status_code = 409
