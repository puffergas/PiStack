from telnetlib import Telnet
# import sys
import socket
import re
# import time

# Telnet, FlightGear Telnet connection
# Copyright (C) 2020 FlightGear <flightgear-devel list>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2 of the License,
# or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330,
# Boston, MA 02111-1307 USA

__all__ = ["FlightGear"]

CRLF = '\r\n'

class FGTelnet(Telnet):
    def __init__(self,host,port):
        Telnet.__init__(self,host,port)
        self.prompt = [re.compile('/[^>]*> '.encode('utf-8'))]
        self.timeout = 5
        #Telnet.set_debuglevel(self,2)

    def help(self):
        return

    def ls(self,dir=None):
        """
        Returns a list of properties.
        """
        if dir is None:
            self._putcmd('ls')
        else:
            self._putcmd('ls %s' % dir )
        return self._getresp()

    def dump(self):
        """Dump current state as XML."""
        self._putcmd('dump')
        return self._getresp()

    def cd(self, dir):
        """Change directory."""
        self._putcmd('cd ' + dir)
        self._getresp()
        return

    def pwd(self):
        """Display current path."""
        self._putcmd('pwd')
        return self._getresp()

    def get(self,var):
        """Retrieve the value of a parameter."""
        self._putcmd('get %s' % var )
        return self._getresp()

    def set(self,var,value):
        """Set variable to a new value"""
        self._putcmd('set %s %s' % (var,value))
        self._getresp() # Discard response

    def quit(self):
        """Terminate connection"""
        self._putcmd('quit')
        self.close()
        return

    # Internal: send one command to FlightGear
    def _putcmd(self,cmd):
        cmd = cmd + CRLF
        Telnet.write(self, cmd.encode('utf-8'))
        return

    # Internal: get a response from FlightGear
    def _getresp(self):
        (_i,_match,resp) = Telnet.expect(self, self.prompt, self.timeout)
        # Remove the terminating prompt.
        # Everything preceding it is the response.
        return resp.decode('utf-8').split('\n')[:-1]

class FlightGear:
    """FlightGear interface class.

    An instance of this class represents a connection to a FlightGear telnet
    server.

    Properties are accessed using a dictionary style interface:
    For example:

    # Connect to flightgear telnet server.
    fg = FlightGear('myhost', 5500)
    # parking brake on
    fg['/controls/gear/brake-parking'] = 1
    # Get current heading
    heading = fg['/orientation/heading-deg']

    Other non-property related methods
    """

    def __init__( self, host = 'localhost', port = 5500 ):
        try:
            self.telnet = FGTelnet(host,port)
        except socket.error as msg:
            self.telnet = None
            raise msg

    def __del__(self):
        # Ensure telnet connection is closed cleanly.
        self.quit()

    def __getitem__(self,key):
        """Get a FlightGear property value.
        Where possible the value is converted to the equivalent Python type.
        """
        s = self.telnet.get(key)[0]
        match = re.compile( r'[^=]*=\s*\'([^\']*)\'\s*([^\r]*)\r').match( s )
        if not match:
            return None
        value,type = match.groups()
        #value = match.group(1)
        #type = match.group(2)
        if value == '':
            return None

        if type == '(double)':
            return float(value)
        elif type == '(int)':
            return int(value)
        elif type == '(bool)':
            if value == 'true':
                return 1
            else:
                return 0
        else:
            return value

    def __setitem__(self, key, value):
        """Set a FlightGear property value."""
        self.telnet.set( key, value )

    def quit(self):
        """Close the telnet connection to FlightGear."""
        if self.telnet:
            self.telnet.quit()
            self.telnet = None

    def view_next(self):
        """Move to next view."""
        self.telnet.set( "/command/view/next", "true")

    def view_prev(self):
        """Move to next view."""
        self.telnet.set( "/command/view/prev", "true")

