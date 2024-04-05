
<h1 align="center">
  Hexakey
</h1>

<div id="header" align="center">
  <img src="https://res.cloudinary.com/zsa-technology/image/upload/f_auto/q_auto/c_scale,w_531/v1/ergodox-ez-prod/images/keyswitches/keyswitches-cherry-brown?_a=BATAV5P80" width="250" height="250">
</div>

# about
hexakey is a simple software using the arduino framework. It communicates when a button is pressed from an arduino to a python script. This python script controls what this button does, whether it will open a file or be a text macro.

# pictures of the hardware it self
<img src="https://raw.githubusercontent.com/skskskye/macro-controller/main/images/PXL_20240405_145322807.jpg?token=GHSAT0AAAAAACQTDJTUWKNM4QNQED5T7UOWZQQDP4Q">

# Libraries used
The libaries used for hexakey are the following:
- pyserial
- threading
- keyboard
- tkinter

# languages usesd
the languages that were used were:
- c++ with the arduino framework
- python 3.12.1

# setup
to setup this software you need to compile the arduino code to an arduino, and just run the py script. make sure that the com port for the ardunio is only opened through one program, if that isnt happening the com port can't be accessed.
