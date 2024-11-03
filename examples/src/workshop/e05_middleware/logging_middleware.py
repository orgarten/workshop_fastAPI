import datetime
import logging
import uuid

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class LoggingMiddleware(BaseHTTPMiddleware):

    logger: logging.Logger

    def __init__(self, app: ASGIApp):
        super().__init__(app)
        handler = logging.StreamHandler()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)

    async def dispatch(self, request: Request, call_next) -> Response:

        request.state.request_id = str(uuid.uuid4())

        self.logger.info(
            "[%s]: Request from '%s' receive at %s",
            request.state.request_id,
            request.headers["host"],
            datetime.datetime.now(datetime.UTC),
        )

        start_time = datetime.datetime.now(datetime.UTC)

        response = await call_next(request)

        processing_time = datetime.datetime.now(datetime.UTC) - start_time

        response.headers["X-Request-ID"] = request.state.request_id


        self.logger.info(
            "[%s]: Request processing time: %s",
            request.state.request_id,
                  processing_time
        )

        self.logger.info(
            "[%s]: Response '%s' for sent at %s",
            request.state.request_id,
            response.status_code,
            datetime.datetime.now(datetime.UTC)
        )

        return response

