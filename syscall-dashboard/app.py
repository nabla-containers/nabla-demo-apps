from tornado import websocket, web, ioloop
import json

cl = []

procs = {}

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

class SocketHandler(websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            print 'new connection'
            cl.append(self)
	    data = {
		'replNabla':'http://172.17.0.2:8081/',
		'replProc':'http://localhost:8081/',
		'dashNabla':'http://localhost:8050/',
		'dashProc':'http://localhost:8051/'}
	    data_json = json.dumps(data)
	    self.write_message(data_json)
	    procs[self] = "user 1"

    def on_close(self):
        if self in cl:
            print 'closed connection'
            cl.remove(self)
	    print procs[self]

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
