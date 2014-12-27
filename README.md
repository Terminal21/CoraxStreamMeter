The Corax StreamMeter
=====================

Platform
--------

Install Raspbian on a RaspberryPI and attach an adafruit MCP4725 DAC.

Installation
------------

Unblock i2c-bcm2708 kernel module.
In file `/etc/modprobe.d/raspi-blacklist.conf` comment out:

    #blacklist i2c-bcm2708

In file `/etc/modules` add:

    i2c-bcm2708
    i2c-dev
  
Load kernel module (or reboot)

    sudo modprobe i2c-bcm2708
    sudo modprobe i2c-dev

Install dependencies

    sudo apt-get install i2c-tools python-smbus

Checkout git repository

    git clone https://github.com/Terminal21/CoraxStreamMeter.git
    cd CoraxStreamMeter

Run the StreamMeter

    sudo python corax.py 

Deployment
----------

For production operating consider to run the CoraxStreamMeter under the control of a process manager like Supervisord.
