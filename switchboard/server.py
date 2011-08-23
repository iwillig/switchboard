"""
Simple WebOb based server for switchboard
"""
from wsgiref.simple_server import make_server
import argparse

from webob import Request, Response

from switchboard import main
from switchboard import log


def do_incoming_message(request, message_router):
    something = message_router(request.query_string)
    return Response(something)


def run_server(config, port=3000):
    """ """
    message_router = main(config)

    def switchboard_app(environ, start_response):
        request = Request(environ)
        if request.path == '/in':
            resp = do_incoming_message(request, message_router)
        else:
            resp = Response('Not found')
        return resp(environ, start_response)

    httpd = make_server('', port=port, app=switchboard_app)
    log.info('Starting server on port %s' % port)
    httpd.serve_forever()


def run_server_command():
    """
    """
    parser = argparse.ArgumentParser(
        description='Process SharedSolar Messages')
    parser.add_argument('config', type=str, help='config file')
    parser.add_argument('port', type=str,
                        default='3000',
                        help='Port to run the server on')
    args = parser.parse_args()
    run_server(args.config, int(args.port))
