Infrequency
===

####Introduction
Is an internet of things radio.

####Configuring the Pi


####Configuring the Pi for the ADXL345
I've borrowed heavily from [Martin O’Hanlon's guide](http://www.stuffaboutcode.com/2014/06/raspberry-pi-adxl345-accelerometer.html).

Add I2C modules
* ```` sudo nano /etc/modules ````
* ```` i2c-bcm2708 ````
* ```` i2c-dev ````

Remove I2C from the blacklist
* ```` sudo nano /etc/modprobe.d/raspi-blacklist.conf ````
* ```` #blacklist i2c-bcm2708 ````

Reboot

Get the i2c stuff
* ```` sudo apt-get install python-smbus i2c-tools git-core ````
* ```` sudo i2cdetect -y 1 ````
