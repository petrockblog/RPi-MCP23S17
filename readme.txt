RPi-MCP23S17
============

This is a Python module that abstracts the GPIO expander MCP23S17. It is intended for the use on a Raspberry Pi.

Provided Functions
------------------

As a quick overview, the module provides the following functions. Refer to the module documentation for details:

 - open
 - close
 - setPullupMode
 - setDirection
 - digitalRead
 - digitalWrite
 - writeGPIO
 - readGPIO

Installation
------------

The module can be installed via PIP with::

	pip install RPi-MCP23S17

Alternatively, you can directly download from this repository .

Example
-------

The following demo peridically toggles all pins of two MCP23S17 components::

	mcp1 = MCP23S17(deviceID=0x00)
	mcp2 = MCP23S17(deviceID=0x01)
	mcp1.open()
	mcp2.open()

	for x in range(0, 16):
	    mcp1.setDirection(x, mcp1.DIR_OUTPUT)
	    mcp2.setDirection(x, mcp1.DIR_OUTPUT)

	print "Starting blinky on all pins (CTRL+C to quit)"
	while (True):
	    for x in range(0, 16):
	        mcp1.digitalWrite(x, MCP23S17.LEVEL_HIGH)
	        mcp2.digitalWrite(x, MCP23S17.LEVEL_HIGH)
	    time.sleep(1)

	    for x in range(0, 16):
	        mcp1.digitalWrite(x, MCP23S17.LEVEL_LOW)
	        mcp2.digitalWrite(x, MCP23S17.LEVEL_LOW)
	    time.sleep(1)
