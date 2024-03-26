import serial
import threading
import keyboard
from tkinter import *
from tkinter import filedialog
import os
import json

port_type = "COM13"
amount_baudrate = 9600

current_location = "location"
current_macro = "macro"



t1 = ""
t2 = ""
t3 = ""
t4 = ""
t5 = ""
t6 = ""

background_color = "#242D61"
button_color = "#C3C3C3"
text_color = "white"

with open(r'Data\macros.json') as file:
    file_contents = json.load(file)
t1input = file_contents["macro1"]
t2input = file_contents["macro2"]
t3input = file_contents["macro3"]
t4input = file_contents["macro4"]
t5input = file_contents["macro5"]
t6input = file_contents["macro6"]

print(t1input, t2input, t3input, t4input, t5input, t6input)


is_macro_on1 = 0
is_macro_on2 = 0
is_macro_on3 = 0
is_macro_on4 = 0
is_macro_on5 = 0
is_macro_on6 = 0

temp_is_macro_on1 = 0
temp_is_macro_on2 = 0
temp_is_macro_on3 = 0
temp_is_macro_on4 = 0
temp_is_macro_on5 = 0
temp_is_macro_on6 = 0

is_program1_open = False
is_program2_open = False
is_program3_open = False
is_program4_open = False
is_program5_open = False
is_program6_open = False

is_connected = False

with open(r'Data\locations.json') as location_file:
    contents = json.load(location_file)

file_to_open1 = contents["file1"]
file_to_open2 = contents["file2"]
file_to_open3 = contents["file3"]
file_to_open4 = contents["file4"]
file_to_open5 = contents["file5"]
file_to_open6 = contents["file6"]

print(file_to_open4)

def handling_ard_input():
    global background_color
    global text_color

    global is_program1_open
    global is_program2_open
    global is_program3_open
    global is_program4_open
    global is_program5_open
    global is_program6_open

    global file_to_open1
    global file_to_open2
    global file_to_open3
    global file_to_open4
    global file_to_open5
    global file_to_open6

    global is_macro_on1
    global is_macro_on2
    global is_macro_on3
    global is_macro_on4
    global is_macro_on5
    global is_macro_on6

    global t1input
    global t2input
    global t3input
    global t4input
    global t5input
    global t6input
    global is_connected
    while is_connected == False:
        try:
            ard = serial.Serial(port = port_type, baudrate = amount_baudrate)
            is_connected = True
            print("connected!")
            break
        except:
            is_connected = False
            #print("error connecting, might not be connected?")
    while True:
        if is_connected == True:  
            data = str(ard.readline())
            #print(data) 
            for i in range(len(data)):
                #Key 1
                if data[i] == "1" and is_program1_open == False:
                    is_program1_open = True
                    if is_macro_on1:
                        print("macro!")
                        keyboard.write(t1input)
                    else:
                        print("opening file!")
                        os.startfile(file_to_open1)
                elif data[i] == "0" and is_program1_open == True:
                    #print("button let go")
                    is_program1_open = False

                #key 2
                if data[i] == "3" and is_program2_open == False:
                    is_program2_open = True
                    if is_macro_on2:
                        print("macro!")
                        keyboard.write(t2input)
                    else:
                        print("opening file!")
                        os.startfile(file_to_open2)
                elif data[i] == "2" and is_program2_open == True:
                    #print("button let go")
                    is_program2_open = False

                #key 3
                if data[i] == "5" and is_program3_open == False:
                    is_program3_open = True
                    if is_macro_on3:
                        print("macro!")
                        keyboard.write(t3input)
                    else:
                        print("opening file!")
                        os.startfile(file_to_open3)
                elif data[i] == "4" and is_program3_open == True:
                    #print("button let go")
                    is_program3_open = False

                #key 4
                if data[i] == "7" and is_program4_open == False:
                    is_program4_open = True
                    if is_macro_on4:
                        print("macro!")
                        keyboard.write(t4input)
                    else:
                        print("opening file!")
                        os.startfile(file_to_open4)
                elif data[i] == "6" and is_program4_open == True:
                    #print("button let go")
                    is_program4_open = False

                #key 5
                if data[i] == "9" and is_program5_open == False:
                    is_program5_open = True
                    if is_macro_on5:
                        print("macro!")
                        keyboard.write(t5input)
                    else:
                        print("opening file!")
                        os.startfile(file_to_open5)
                elif data[i] == "8" and is_program5_open == True:
                    #print("button let go")
                    is_program5_open = False
                
                #key 6
                if data[i] == "w" and is_program6_open == False:
                    is_program6_open = True
                    print(data[i])
                    if is_macro_on6:
                        print("macro!")
                        keyboard.write(t6input)
                    else:
                        print("opening file!")
                        os.startfile(file_to_open6)
                elif data[i] == "q" and is_program6_open == True:
                    #print("button let go")
                    is_program6_open = False
        else:
            print("connection failed! arduino possibly not plugged in?")

def clicked():
    global is_connected

    global is_macro_on1
    global is_macro_on2
    global is_macro_on3
    global is_macro_on4
    global is_macro_on5
    global is_macro_on6

    is_macro_on1 = temp_is_macro_on1.get()
    is_macro_on2 = temp_is_macro_on2.get()
    is_macro_on3 = temp_is_macro_on3.get()
    is_macro_on4 = temp_is_macro_on4.get()
    is_macro_on5 = temp_is_macro_on5.get()
    is_macro_on6 = temp_is_macro_on6.get()

    print("1: ", is_macro_on1)
    print("2: ", is_macro_on2)
    print("3: ", is_macro_on3)
    print("4: ", is_macro_on4)
    print("5: ", is_macro_on5)
    print("6: ", is_macro_on6)
    
def apply_macro():
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6

    global t1input
    global t2input
    global t3input
    global t4input
    global t5input
    global t6input
    
    t1input = t1.get(1.0, "end-1c")     
    t2input = t2.get(1.0, "end-1c")
    t3input = t3.get(1.0, "end-1c")
    t4input = t4.get(1.0, "end-1c")
    t5input = t5.get(1.0, "end-1c")
    t6input = t6.get(1.0, "end-1c")

    data = {
            'macro1': t1input, 
            'macro2': t2input, 
            'macro3': t3input,
            'macro4': t4input,
            'macro5': t5input,
            'macro6': t6input
            }
    
    with open(r"data\macros.json", 'w') as f:
        json.dump(data, f)
    print(data)


def window():
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6
    
    global temp_is_macro_on1
    global temp_is_macro_on2
    global temp_is_macro_on3
    global temp_is_macro_on4
    global temp_is_macro_on5
    global temp_is_macro_on6

    
    global background_color
    global button_color
    global text_color
    
    #dimensions
    x_dimension = 500
    y_dimension = 480

    #window config
    window = Tk()
    window.title("Hexakey")
    window.resizable(0,0)
    window.geometry(f"{x_dimension}x{y_dimension}")
    window.iconbitmap("icon.ico")
    window.configure(bg=background_color)

    #title
    title = Label(window, text="HEXAKEY")
    title.config(font=("Pixellari", 35), bg=background_color, fg=text_color)

    #textfield 1
    t1 = Text(window, height = 1, width=20)
    t1.place(x=325,y=73)

    #textfield 2
    t2 = Text(window, height = 1, width=20)
    t2.place(x=325,y=133)

    #textfield 3
    t3 = Text(window, height = 1, width=20)
    t3.place(x=325,y=193)

    #textfield 4
    t4 = Text(window, height = 1, width=20)
    t4.place(x=325,y=253)

    #textfield 5
    t5 = Text(window, height = 1, width=20)
    t5.place(x=325,y=313)

    #textfield 6
    t6 = Text(window, height = 1, width=20)
    t6.place(x=325,y=373)

    #checkbox 1
    temp_is_macro_on1 = IntVar()
    checkbox1 = Checkbutton(window, text="Text macro?", variable=temp_is_macro_on1, command=clicked, onvalue=1, offvalue=0)
    checkbox1.place(x=225,y=70)

    #checkbox 2
    temp_is_macro_on2 = IntVar()
    checkbox2 = Checkbutton(window, text="Text macro?", variable=temp_is_macro_on2, command=clicked, onvalue=1, offvalue=0)
    checkbox2.place(x=225,y=135)

    #checkbox 3
    temp_is_macro_on3 = IntVar()
    checkbox3 = Checkbutton(window, text="Text macro?", variable=temp_is_macro_on3, command=clicked, onvalue=1, offvalue=0)
    checkbox3.place(x=225,y=195)

    #checkbox 4
    temp_is_macro_on4 = IntVar()
    checkbox4 = Checkbutton(window, text="Text macro?", variable=temp_is_macro_on4, command=clicked, onvalue=1, offvalue=0)
    checkbox4.place(x=225,y=255)

    #checkbox 5
    temp_is_macro_on5 = IntVar()
    checkbox5 = Checkbutton(window, text="Text macro?", variable=temp_is_macro_on5, command=clicked, onvalue=1, offvalue=0)
    checkbox5.place(x=225,y=315)

    #checkbox 6
    temp_is_macro_on6 = IntVar()
    checkbox6 = Checkbutton(window, text="Text macro?", variable=temp_is_macro_on6, command=clicked, onvalue=1, offvalue=0)
    checkbox6.place(x=225,y=375)

    #button 1
    button1_label = Label(window, text="Key 1")
    button1_label.config(font=("Pixellari", 15), bg=background_color, fg=text_color)
    button1_label.place(y = 75, x = 25)
    b = Button(window, text="Click to chose file", command=lambda : get_file_dir(1), height=3, width=15)
    b.config(bg=button_color)
    b.place(x = 100, y = 60)
    
    

    #button 2
    button2_label = Label(window, text="Key 2")
    button2_label.config(font=("Pixellari", 15), bg=background_color, fg=text_color)
    button2_label.place(y = 135, x = 25)
    b2 = Button(window, text="Click to chose file", command=lambda : get_file_dir(2), height=3, width=15)
    b2.config(bg=button_color)
    b2.place(x = 100, y = 120)

    #button 3
    button2_label = Label(window, text="Key 3")
    button2_label.config(font=("Pixellari", 15), bg=background_color, fg=text_color)
    button2_label.place(y = 195, x = 25)
    b2 = Button(window, text="Click to chose file", command=lambda : get_file_dir(3), height=3, width=15)
    b2.config(bg=button_color)
    b2.place(x = 100, y = 180)

    #button 4
    button2_label = Label(window, text="Key 4")
    button2_label.config(font=("Pixellari", 15), bg=background_color, fg=text_color)
    button2_label.place(y = 255, x = 25)
    b2 = Button(window, text="Click to chose file", command=lambda : get_file_dir(4), height=3, width=15)
    b2.config(bg=button_color)
    b2.place(x = 100, y = 240)

    #button 5
    button2_label = Label(window, text="Key 5")
    button2_label.config(font=("Pixellari", 15), bg=background_color, fg=text_color)
    button2_label.place(y = 315, x = 25)
    b2 = Button(window, text="Click to chose file", command=lambda : get_file_dir(5), height=3, width=15)
    b2.config(bg=button_color)
    b2.place(x = 100, y = 300)

    #button 6
    button2_label = Label(window, text="Key 6")
    button2_label.config(font=("Pixellari", 15), bg=background_color, fg=text_color)
    button2_label.place(y = 375, x = 25)
    b2 = Button(window, text="Click to chose file", command=lambda : get_file_dir(6), height=3, width=15)
    b2.config(bg=button_color)
    b2.place(x = 100, y = 360)

    #apply button
    apply = Button(window, text="Apply macro", command=apply_macro, height=3, width=22)
    apply.config(bg=button_color)
    apply.place(x = 325, y = 410)

    #layout button this is the bane of my existance 

    # layout = Button(window, text="Layouts", command=layout_window, height=1, width=6 )
    # layout.config(bg=button_color)
    # layout.place(x=10, y=10)

    #packinge elements
    title.pack()

    #looping ui
    window.mainloop()   

# # def layout_window(): i HATE this :c
#     global background_color
#     global button_color
#     global text_color
#     root = Tk()
#     root.geometry("200x200")
#     root.configure(bg=background_color)
#     root.title("layouts")

#     #location stuff
#     location_options = [
#         "location1",
#         "location2",
#         "location3"
#     ]

#     #macro stuff 
#     macro_options = [
#         "macro1",
#         "macro2",
#         "macro3"
#     ]

#     #dropdown itself

#     clicked = StringVar()

#     macro_drop = OptionMenu(root, clicked, *macro_options)
#     macro_drop.pack()

#     root.mainloop()
    

def on_click(type):
    global current_location
    global current_macro

    if type == "macro":
        current_macro = clicked.get()
    if type == "location":
        current_location = clicked.get()
def get_file_dir(button):

    #global vars
    global file_to_open1
    global file_to_open2
    global file_to_open3
    global file_to_open4
    global file_to_open5
    global file_to_open6
    
    #logic for what button pressed
    if button == 1:
        file_to_open1 = filedialog.askopenfilename()
        print(file_to_open1)
    elif button == 2:
        file_to_open2 = filedialog.askopenfilename()
        print(file_to_open2)
    elif button == 3:
        file_to_open3 = filedialog.askopenfilename()
        print(file_to_open3)
    elif button == 4:
        file_to_open4 = filedialog.askopenfilename()
        print(file_to_open4)
    elif button == 5:
        file_to_open5 = filedialog.askopenfilename()
        print(file_to_open5)
    elif button == 6:
        file_to_open6 = filedialog.askopenfilename()
        print(file_to_open6)
    
    data = {
        "file1": file_to_open1, 
        "file2": file_to_open2, 
        "file3": file_to_open3, 
        "file4": file_to_open4, 
        "file5": file_to_open5, 
        "file6": file_to_open6
        }
    print(data)
    with open(r"data\locations.json", "w") as f:
        json.dump(data, f)
        
    

    
    
    

#threading
t1 = threading.Thread(target=handling_ard_input)
t2 = threading.Thread(target=window)

#starting the threads
t1.start()
t2.start()

