#Code de M. Roussel

from http.server import BaseHTTPRequestHandler, \
    HTTPServer
import pymysql

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        headerHTML = open("4-25-5-header.html")
        footerHTML = open("4-25-6-footer.html")
        message = headerHTML.read()
        message += '<h1>TITRE</h1>'

        db = pymysql.connect(host='localhost',
                             #port=3306,
                             user='python',
                             password='onyva',
                             database='python1')
        cur = db.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT item FROM exo20160425")
        message += "<ul>"
        for row in cur:
            message += "<li>" + row['item'] + "</li>"
        message += "</ul>"

        message += footerHTML.read()
        headerHTML.close()
        footerHTML.close()
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally
  # used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address,
                     testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
