
<h1 align="center">
  Hexakey
</h1>

# About
Hexakey is a simple software using the Arduino framework. It communicates when a button is pressed from an Arduino to a Python script. This Python script controls what this button does, whether it will open a file or be a text macro.

# Pictures of the hardware it self
<img src="https://raw.githubusercontent.com/skskskye/macro-controller/main/images/PXL_20240405_145322807.jpg?token=GHSAT0AAAAAACQTDJTUWKNM4QNQED5T7UOWZQQDP4Q">

# Libraries used
The libraries used for hexakey are the following:
- pyserial
- threading
- keyboard
- tkinter

# Languages ussd
The languages that were used were:
- c++ with the arduino framework
- python 3.12.1

# Setup
to set up this software, you need to compile the Arduino code to an Arduino and just run the py script. Make sure the Arduino COM port is open in only one program; if it isn't, the COM port can't be accessed.
