"""
Simple HTTP server prints "Hello World!" page.

Reads in a json config as the first argument that contains the port, host,
sha1 hash and password salt.

The returned page shows information about the incoming request as
well as authentication status.
"""
import hashlib
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys

# Config to be loaded from a file specified
# by command line argument
CONF = None

# Template string for the generated html response
PAGE_FMTSTR = """\
<html>
<head><title>Hello World</title></head>
<body>
<h1>Hello World!</h1>
<br />
<h3>Special Message: {message}</h3>
<br />
This was a {method} request.
<br />
The request path was {path}.
<br />
The request body was {body}.
<br />
The sha1 is {sha1}.
<br />
The salt is {salt}.
<br />
<br />
Authentication was {auth_status}.
<br />
<br />
Server running python version {version}.
</body>
</html>
"""


class HelloHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Handler class to respond to GET and POST requests by returning
    a brief HTML page with some diagnostic information about the
    request.
    """
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response = PAGE_FMTSTR.format(
            method="GET",
            sha1=CONF['sha1'],
            salt=CONF['salt'],
            body="",
            path=self.path,
            auth_status='not attempted',
            message=CONF['message'],
            version=sys.version
        )
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        self.send_response(200)
        self.end_headers()
        if check_auth(body):
            auth_status = 'successful'
        else:
            auth_status = 'failed'
        response = PAGE_FMTSTR.format(
            method="POST",
            sha1=CONF['sha1'],
            salt=CONF['salt'],
            body=body,
            path=self.path,
            auth_status=auth_status,
            message=CONF['message'],
            version=sys.version
        )
        self.wfile.write(response.encode('utf-8'))


def check_auth(body):
    """
    Run through the & delimited fields of the request body
    and check the contents of any password field against
    our configured hash.

    Return True if the salted and hashed password matches.
    """
    try:
        fields = body.split('&')
        for item in fields:
            key, val = item.split('=')
            if key == 'password':
                salted = (val + CONF['salt']).encode('utf-8')
                sha1 = hashlib.sha1(salted)
                if sha1.hexdigest() == CONF['sha1']:
                    return True
    except Exception:
        pass
    return False


def main():
    """
    Read in the configuration global from the file provided on the command
    line and start the server
    """
    global CONF
    CONF = json.loads(open(sys.argv[1]).read())
    httpd = HTTPServer(('0.0.0.0', CONF['port']), HelloHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
