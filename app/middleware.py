import os
import time
import uuid
from app.logger import get_logger

from flask import g, request


def register_middlewares(app):

    logger = get_logger(__name__)

    @app.before_request
    def before_request():

        g.start_time = time.time()

        g.request_id = str(uuid.uuid4())

    @app.after_request
    def after_request(response):

        duration = round((time.time() - g.start_time) * 1000, 2)

        logger.info(
            "HTTP Request",
            extra={
                "request_id": g.request_id,
                "method": request.method,
                "path": request.path,
                "status": response.status_code,
                "duration_ms": duration,
                "remote_addr": request.remote_addr,
                "pod": os.getenv("HOSTNAME"),
                "service": "employee-api",
                "version": "1.0.0",
            },
        )

        return response
