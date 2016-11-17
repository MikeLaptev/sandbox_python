__author__ = 'mlaptev'


def wsgi_application(environ, start_response):
    status = '200 Ok'
    headers = [('Content-Type', 'text/plain')]
    body = ['']
    if 'QUERY_STRING' in environ:
        body = environ['QUERY_STRING'].split('&')
    start_response(status, headers)
    return body
