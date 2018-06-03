from tornado import websocket, web, ioloop
import pexpect
import subprocess
import json
import os
import signal
from pexpect.popen_spawn import PopenSpawn

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
            cmd_dashNabla = "stdbuf --output=0 sysdig proc.pid=29676 -c countsc | python dash_histo.py --port 8050"


            ps_nabla = pexpect.spawn('/bin/bash', ['-c', cmd_dashNabla], timeout=None)
            fout = open('mylog.txt','wb')
            ps_nabla.logfile = fout
            ps_nabla.expect("Running on http")

            cmd_dashProc = "stdbuf --output=0 sysdig proc.name=node -c countsc | python dash_histo.py --port 8051"
            ps_proc = pexpect.spawn('/bin/bash', ['-c', cmd_dashProc], timeout=None)
            ps_proc.expect("Running on http")

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
