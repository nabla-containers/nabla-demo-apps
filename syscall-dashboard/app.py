from tornado import websocket, web, ioloop
import subprocess
import json
import os
import signal

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
            cmd_dashNabla = "python dash_histo.py --port 8050 --pid ukvm-bin"
            ps_nabla = subprocess.Popen(cmd_dashNabla, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)
            while ps_nabla.stderr.readline() == '': pass

            cmd_dashProc = "python dash_histo.py --port 8051 --pid node"
            ps_proc = subprocess.Popen(cmd_dashProc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)
            while ps_proc.stderr.readline() == '': pass

            data = {
                'replNabla':'http://172.17.0.2:8081/',
                'replProc':'http://localhost:8081/',
                'dashNabla':'http://localhost:8050/',
                'dashProc':'http://localhost:8051/'}
            data_json = json.dumps(data)
            self.write_message(data_json)
            cl.append(self)
            procs[self] = (ps_nabla, ps_proc)
            print('new connection')
            print(procs[self])

    def on_close(self):
        if self in cl:
            print('closed connection')
            cl.remove(self)
            ps_nabla, ps_proc = procs[self]
            print(procs[self])
            os.killpg(os.getpgid(ps_nabla.pid), signal.SIGTERM)  # Send the signal to all the process groups
            os.killpg(os.getpgid(ps_proc.pid), signal.SIGTERM)  # Send the signal to all the process groups

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
])

if __name__ == '__main__':
    app.listen(8888)
    try:
            ioloop.IOLoop.instance().start()
    finally:
            for (ps_nabla, ps_proc) in procs.values():
                    os.killpg(os.getpgid(ps_nabla.pid), signal.SIGTERM)  # Send the signal to all the process groups
                    os.killpg(os.getpgid(ps_proc.pid), signal.SIGTERM)  # Send the signal to all the process groups
