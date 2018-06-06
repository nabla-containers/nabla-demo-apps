import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        size = int(self.get_argument('size', 1000))
        self.write('x'*size)

    def post(self):
        size = int(self.get_argument('size', 1000))
        self.write('x'*size)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
