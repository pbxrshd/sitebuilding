#!/usr/bin/python

import BaseHTTPServer
import SimpleHTTPServer
import serial

HTTP_PORT = 56789

def execute_command(commandData):
    global SERIAL_REF
    if 'o' == commandData:
        return 'ok - opened'
    elif 'c' == commandData:
        return 'ok - closed'
    else:
        return 'other response'

class SimpleHTTPHandlerImpl(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            #serve files, and directory listings by following self.path from current working directory
            print ':',self.path,':'
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        except:
            result = '<html><body>error...</body></html>'
            self.wfile.write(result)
    def do_POST(self):
        """Handle a post request"""
        length = int(self.headers.getheader('content-length'))        
        data_string = self.rfile.read(length)
        result = execute_command(data_string)
        self.wfile.write(result)

def main():
    server = BaseHTTPServer.HTTPServer(("localhost", HTTP_PORT), SimpleHTTPHandlerImpl)
    try:
        print "serving at port", HTTP_PORT
        server.serve_forever()
    except KeyboardInterrupt:
        print 'shutting down...'
        server.socket.close()
        
if __name__ == '__main__':
    main()   
