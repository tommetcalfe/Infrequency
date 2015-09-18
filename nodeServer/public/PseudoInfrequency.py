import stuff
accel = adxl345.ADXL345()

M_PI = 3.141592

stopLatch = False;
playLatch = False;

ssePath = "/path";

x = 0;
y = 0;
z = 0;


#----------------------------------------------------
def setupAccel():
    accel.setRange(adxl345.RANGE_2G)
    accel.setRange(adxl345.RANGE_4G)
    accel.setRange(adxl345.RANGE_8G)
    accel.setRange(adxl345.RANGE_16G)

#----------------------------------------------------
def sendStopEvent():
    #SSE Events
    sse.send(ssePath, "stop");
    playLatch = False;

#----------------------------------------------------
def sendPlayEvent():
    sse.send(ssePath, "play");
    !stopLatch = False;

#----------------------------------------------------
def main_loop():



    while 1:
        # Get the Angle converted into degrees
        xyz = convertAccelToAngle(accel.getAxis())
        print xyz;
        
        # Angle relates to the return angle from the Accelorometer
        # So if the sensor is beyond both positive or negative angles
        # trigger the stop signal;
        if xyz > angle | xyz < -angle & stopLatch:
            sendStopEvent();
            stopLatch = False;
            playLatch = True;

        # If the angle of the Accelorometer settles within range
        # Flip the latch and send the Play signal to the Server
        elif xyz >= settledAngle & xyz <= settledAngle & playLatch:
            sendPlayEvent();
            playLatch = False;
            stopLatch = False;


#----------------------------------------------------
# Function to return the degrees from the Accelorometer
def convertAccelToAngle(x,y,z):
    roll = (math.atan2(-y,z)*180)/M_PI
    pitch = (math.atan2(x,math.sqrt(y*y + z*z))*180)/M_PI
    yaw = (math.atan(math.sqrt(x)+math.sqrt(y)/z)*180)/M_PI
    return roll,pitch,yaw

#----------------------------------------------------
if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
