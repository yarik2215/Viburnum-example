
from viburnum.application import route, Request, Response


@route("/hello", methods=['ANY'])
def hello(request: Request) -> Response:
    return Response(200, {})

