RPiMCP23S17
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

If not already done, you need to install PIP via::

	sudo apt-get install python-pip

Install from `PyPI <https://pypi.python.org/pypi/RPiMCP23S17>`_::

	pip install RPiMCP23S17

Example
-------

The following demo peridically toggles all pins of two MCP23S17 components::

	from RPiMCP23S17.MCP23S17 import MCP23S17
	import time

	mcp1 = MCP23S17(bus=0x00, ce=0x00, deviceID=0x00)
	mcp2 = MCP23S17(bus=0x00, ce=0x00, deviceID=0x01)
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
		    
		    # the lines below essentially have the same effect as the lines above
		    mcp1.writeGPIO(0xFFF)
		    mcp2.writeGPIO(0xFFF)
		    time.sleep(1)
		    
		    mcp1.writeGPIO(0x000)
		    mcp2.writeGPIO(0x0000)
		    time.sleep(1)

