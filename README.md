
<h1 align="center">
  Hexakey
</h1>

# About
Hexakey is a simple software using the Arduino framework. It communicates when a button is pressed from an Arduino to a Python script. This Python script controls what this button does, whether it will open a file or be a text macro.

# Pictures of the hardware itself
To see the pictures of the hardware, go into the images folder in the repo

# Libraries used
The libraries used for hexakey are the following:
- pyserial
- threading
- keyboard
- tkinter

# Languages used
The languages that were used were:
- C++ with the Arduino framework
- Python 3.12.1

# Setup
to set up this software, you need to compile the Arduino code to an Arduino and just run the py script. Make sure the Arduino COM port is open in only one program; if it isn't, the COM port can't be accessed.
