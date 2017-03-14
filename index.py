from cgi import parse_qs, escape


def application(env, start_response):
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = env['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [str(d)]
