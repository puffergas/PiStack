<h1 style="text-align: center;" markdown="1">PiStack</h1>
<h4 style="text-align: center;" markdown="1">Version 0.4.1-beta</h4>

![Main Screen](https://i.imgur.com/An9qOjD.png)

![Keypad](https://i.imgur.com/oJJ0eg4.png)

## Intro:
PiStack is a remote radio interface for FlightGear, that is designed to
work with the Raspberry Pi Official thouch screen.However it should run
on other devices that can run Python3.

## License:
PiStack, a remote radio stack for FlightGear
Copyright (C) 2020 Jeffrey Davis <jeff@puffergas.com>

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the:
Free Software Foundation, Inc.,
59 Temple Place, Suite 330,
Boston, MA 02111-1307 USA

## Dependencies
1. Python 3
2. PySimpleGUI

## Logic Holes:
* FlightGear needs to be configured and running before PiStack can run.
* PiStack will go out of sync if radio settings are changed from within FlightGear.
* PiStack was written for and tested on/for the DC-3

## Installation:
The below installation is written for the Raspberry Pi, however other devices that can run Python will be somewhat similar.

## Abbreviated installation:
* Install the Python module PySimpleGUI.
* Create a folder called PiStack in your home directory. For example `home/pi`.
* Populate the above folder with pistack.py and telnet.py.

## More detailed installation:
* Install PySimpleGUI. This can be copied into the below folder  with the file found at [https://pypi.org/project/PySimpleGUI/](URL) Look for the Download files link.
* Or use `pip3`. Or  something like `python3 -m pip install PySimpleGUI`
* Create a folder called PiStack in your home directory. For example `home/pi/PiStack`.
* Go to [https://github.com/puffergas/PiStack](URL) to find the needed PiStack files and place them into the PiStack folder that you created. The files pistack.py and telnet.py are needed.
* In order to make it easier to start PiStack, there is an icon and .desktop file to add PiStack to the launcher menu and or have a desktop shortcut. If used on a different device or if files are located somewhere else, the PiStack.desktop file will need edited.
    * Place PiStack_Icon.png file in to the PiStack folder that you created.
    * Place PiStack.desktop into `/home/pi/.local/share/applications`
    * PiStack.desktop can also be placed on the Desktop, as an option.

## Configuring FlightGear:
![Telnet](http://wiki.flightgear.org/images/b/b8/Setup_for_Telnet.png)  
In the FlightGear launcher, place the command --telnet=####, where “####” is the port number.

## Configuring PiStack:
At this time the file pistack.py needs edited, in order to configure PiStack. Use a text editor or an IDE to edit the file. Find the below two lines. They should be near line number 25 and 26.


    25 fg = FlightGear('localhost', 5401)
    26 # fg = FlightGear('192.168.##.#', 5401)

Notice that on line number 25 (above), that there is no # symbol. That means that line 25 is active (not committed out). In this case, PiStack is running on the same Raspberry (computer) as FlightGear, hence localhost. The number 5401 is the port number. This needs to be the same port number as configured in FlightGear.

Below we have configured PiStack to be used on a remote device, via your home network. Notice that line 25 has been committed out and now line 26 is now active. The address '192.168.##.#' will need to be edited to match the address of the Raspberry (computer) running FlightGear.

    25 # fg = FlightGear('localhost', 5401)
    26 fg = FlightGear('192.168.##.#', 5401)

Don’t forget to save the file.   😉

## Bugs and Issues:
* At this time, PiStack has been tested and written for the DC-3.
* Some aircraft Nasal code may interfere with some of the PiStack’s settings. Possible examples may be the volume and On Off button.

