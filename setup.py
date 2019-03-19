"""
Copyright (c) 2016 - Florian Mueller

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# from distutils.core import setup, Extension
import setuptools

classifiers = ['Development Status :: 5 - Production/Stable',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware']

setuptools.setup(
      name             = 'RPiMCP23S17',
      version          = '1.0.0',
      author           = 'Florian Mueller',
      author_email     = 'contact@petrockblock.com',
      description      = 'A module to access GPIO expanders MCP23S17 from a Raspberry Pi.',
      long_description = open('README.txt').read() + open('CHANGELOG.txt').read(),
      license          = 'MIT',
      keywords         = 'Raspberry Pi GPIO MCP23S17 SPI',
      url              = 'http://github.com/petrockblog/RPi-MCP23S17',
      classifiers      = classifiers,
      install_requires = ['RPi.GPIO',
                          'spidev'],
      packages         = ['RPiMCP23S17'])
