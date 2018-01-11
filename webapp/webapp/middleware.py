import uuid

import structlog


logger = structlog.get_logger()


def add_request_id(get_response):
    def middleware(request):
        request_id = str(uuid.uuid4())
        logger.new(
            request_id=request_id,
        )
        request.request_id = request_id
        response = get_response(request)
        return response

    return middleware
