import http.cookies

def application(environ, start_response):
    response_headers = [('Content-type', 'text/html; charset=utf-8')]
    
    method = environ["REQUEST_METHOD"]
    
    if method == "GET":
      status = '403 Forbidden'
      content = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Dog Global Database</title>
  </head>
  <body>
    <h1>403 Forbidden</h1>
    <p>We are unsure that you're dog.</p>
    <p>If you're real dog, you know that you should use another method to see this database.</p>
    <hr/>
    <p>Dog Association</p>
  </body>
</html>
'''
    elif method == "PUT":
      status = '200 OK'
      content = '''<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <h1>Urgent Request</h1>
    <p>Who can take this info to Moscow office?</p>
    <p><code>Very secret info visible only to dogs</code><!-- uctf_use_put_instead_of_get --></p>
  </body>
</html>
'''
    else:
      status = '405 Method Not Allowed'
      content = '''<h1>Unsupported method</h1>'''
    
    content = content.encode('utf-8')
    clh = ('Content-Length', str(len(content)))
    response_headers.append(clh)

    start_response(status, response_headers)

    return [content]
