from tornado import websocket, web, ioloop
import pexpect
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
	    #dashNabla = pexpect.spawn('sudo stdbuf --output=0 sysdig proc.name=ukvm-bin -c countsc | python dash_histo.py --port 8050')
	    #dashNabla = pexpect.spawn('sysdig proc.name=ukvm-bin -c countsc | python dash_histo.py --port 8050')
	    logs = open('out-file.txt', 'w')
	    #cmd = "sudo stdbuf --output=0 sysdig proc.name=ukvm-bin -c countsc | python dash_histo.py --port 8050"
	    cmd = "stdbuf --output=0 sysdig proc.name=ukvm-bin -c countsc | python dash_histo.py --port 8050"
	    #ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=logs, preexec_fn=os.setsid)
	    ps = subprocess.Popen(cmd,shell=True,stdout=logs,stderr=logs, preexec_fn=os.setsid)
	    data = {
		'replNabla':'http://172.17.0.2:8081/',
		'replProc':'http://localhost:8081/',
		'dashNabla':'http://localhost:8050/',
		'dashProc':'http://localhost:8051/'}
	    data_json = json.dumps(data)
	    self.write_message(data_json)
            cl.append(self)
	    procs[self] = ps
            print 'new connection'
	    print procs[self]

    def on_close(self):
        if self in cl:
            print 'closed connection'
            cl.remove(self)
	    ps = procs[self]
	    print procs[self]
	    os.killpg(os.getpgid(ps.pid), signal.SIGTERM)  # Send the signal to all the process groups

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
])

if __name__ == '__main__':
    app.listen(8888)
    try:
	    ioloop.IOLoop.instance().start()
    finally:
	    for ps in procs.values():
	    	os.killpg(os.getpgid(ps.pid), signal.SIGTERM)  # Send the signal to all the process groups
