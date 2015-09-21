Infrequency
===

####Introduction
Is an Internet of Things radio.

####Components
* 1x Raspberry Pi
* 1x ADXL345 Accelerometer
* 1x InfrequencyServer.py
* 1x InfrequencySensor.py
* 1x launchInfrequency.sh
* 1x stopInfrequency.sh

####Configuring the Pi
#####Dependencies
Infrequency has the following dependencies.

* ````sudo pip install tornado flask bottle matchbox chromium x11-xserver-utils ttf-mscorefonts-installer xwit sqlite3 libnss3 git````

Pull this repo
* ````git clone https://github.com/DHaylock/Infrequency.git````

Move the `xinitrc` file to the `/home/pi`
* ````cd Infrequency/ ````
* ````mv xinitrc ../ ````

#####WiFi
You will need to configure the WiFi

First identify the network
* ````sudo iwlist wlan0 scan````

Make a note of the ESSID name
* ````sudo nano /etc/wpa_supplicant/wpa_supplicant.conf````

Add the following lines to the config file
* `network={ssid="ESSID"
    psk="Your_wifi_password"}`

Reset the network
* ````sudo ifdown wlan0````
* ````sudo ifup wlan0````
* ````sudo reboot````

Once rebooted verify the connection to the WiFi Network
* ````ifconfig wlan0````

#####Changing the Hostname
You will need to change the hostname
* ````sudo nano /etc/hostname````

Save the name then commit the changes
* ````sudo /etc/init.d/hostname.sh````

Then Reboot
* ````sudo reboot````

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

####Configuring the ADXL345
I came across a strange error with the breakout board and the i2ctools did not recognise the device. My solution was to connect the `cs` pin to the 3v3 output.

![Schematic](./images/Infrequency_schem.jpg "Schematic")

The wiring otherwise involves:

| ADXL345  | RPi |
|---|---|
| GND | GND (pin 9) |
| Vcc | 3v3 (pin 1) |
| SDA | SDA (pin 3) |
| SCL | SCL (pin 5) |
| CS  | 3v3 (pin 17) |
| INT1 | NC |
| INT2 | NC |

####
