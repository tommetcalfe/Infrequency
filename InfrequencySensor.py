import os.path
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import time
import datetime
import time
from adxl345 import ADXL345
import math

M_PI = 3.141592
adxl345 = ADXL345()

#----------------------------------------------------
# Function to return the degrees from the Accelorometer
def convertAccelToAngle(x,y,z):
    roll = (math.atan2(-y,z)*180)/M_PI
    pitch = (math.atan2(x,math.sqrt(y*y + z*z))*180)/M_PI
#    yaw = (math.atan(math.sqrt(x)+math.sqrt(y)/z)*180)/M_PI
    return roll,pitch

# while 1:
# 	axes = adxl345.getAxes(False)
# 	xy = convertAccelToAngle(axes['x'],axes['y'],axes['z'])
# 	print xy
# 	if xy[0] > -10.000 and xy[0] < 10.000:
# 		print "settled"
# 	else:
# 		print "argh"
# 	time.sleep(0.2)


#-----------------------------------------------------------------
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'New Connection'
        self.write_message("Hello, we've opened and Connected to you")
        # tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=1), self.play)

    def on_message(self, message):
        print 'Message received: \"%s\"' % message
        self.write_message("Echo: \"" + message + "\"")

    def on_close(self):
        print 'connection closed'

    def check_origin(self, origin):
        return True

    def play(self):
        self.write_message("play")

    def stop(self):
        self.write_message("stop")

    def shuffle(self):
        self.write_message("shuffle")

    def checkLeftb(self):
        self.write_message("play")
#-----------------------------------------------------------------
handlers = [
    (r'/ws', WSHandler),
]

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "static"),
)

application = tornado.web.Application(handlers, **settings)

#----------------------------------------------------
def main_loop():
    print "hello"

#----------------------------------------------------
if __name__ == '__main__':

    print "ADXL345 on address 0x%x:" % (adxl345.address)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8001)
    tornado.ioloop.IOLoop.current().run_sync(WSHandler.play)
    # tornado.ioloop.IOLoop.instance().start()

    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
