from viburnum.application import route, Request, Response

from shared.utils import say_hello

@route("/")
def sample_func(request: Request) -> Response:
    say_hello()
    return Response(200, {})
