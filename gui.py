import os

from plot2 import show

try:
    import customtkinter
except ImportError:
    os.system('pip install customtkinter')
    import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Graph Viewer (Millard North Team 1)")
root.geometry("1050x600")  # If running this code on Linux with Wayland graphics, use "1300x650" instead of "1000x600"
root.resizable(False, False)

color_blindness_index = 0

disp = customtkinter.CTkLabel(root, text="  ", font=("Ariel", 20))
disp.grid(row=0, column=4, padx=10)


def click1():
    global disp
    disp.configure(text='A separate window is\nnow displaying Graph 1')
    show(slider.get(), color_blindness_index)


# functions to change color mode, change graph color variables with these functions
def colormode_update1():
    global colormode_label
    colormode_label.configure(text="")
    colormode_label = customtkinter.CTkLabel(root, text="Color mode set\nto DEUTERANOPIA", font=("Ariel", 20),
                                             text_color='#A27A01')
    colormode_label.grid(row=5, column=4, padx=10)
    global color_blindness_index
    color_blindness_index = 1


# change colors in graph for deuteranopia


def colormode_update2():
    global colormode_label
    colormode_label.configure(text="")
    colormode_label = customtkinter.CTkLabel(root, text="Color mode set\nto PROTANOPIA", font=("Ariel", 20),
                                             text_color='#008ff5')
    colormode_label.grid(row=5, column=4, padx=10)
    global color_blindness_index
    color_blindness_index = 2


# change colors in graph for protanopia


def colormode_update3():
    global colormode_label
    colormode_label.configure(text="")
    colormode_label = customtkinter.CTkLabel(root, text="Color mode set\nto TRITANOPIA", font=("Ariel", 20),
                                             text_color='#EE3168')
    colormode_label.grid(row=5, column=4, padx=10)
    global color_blindness_index
    color_blindness_index = 3


# change colors in graph for tritanopia


def defaultcmode():
    global colormode_label
    colormode_label.configure(text="")
    colormode_label = customtkinter.CTkLabel(root, text="Color mode set\nto DEFAULT", font=("Ariel", 20))
    colormode_label.grid(row=5, column=4, padx=10)
    global color_blindness_index
    color_blindness_index = 0


colormode_label = customtkinter.CTkLabel(root, text="Color mode set\nto DEFAULT", font=("Ariel", 20))
colormode_label.grid(row=5, column=4, padx=10)

# graph button header
viewg = customtkinter.CTkLabel(root, text="View graph:", font=("Ariel", 20))
viewg.grid(row=0, column=0, padx=15)

# graph buttons
g1 = customtkinter.CTkButton(root, text="Average Snowfall\nvs\nScour Scores", command=click1, font=("Ariel", 20),
                             height=150,
                             width=250, hover_color='#7d0000', fg_color='red')  # actual buttons that do above commands
g1.grid(row=0, column=1, padx=10, pady=10, sticky="ewns")

# color buttons header
cbfunct = customtkinter.CTkLabel(root, text="Set color mode\nfor color-blindness:", font=("Ariel", 20))
cbfunct.grid(row=5, column=0, padx=15, pady=10)

filler_a = customtkinter.CTkLabel(root, text="        \n      ", font=("Ariel", 20))
filler_a.grid(row=6, column=0, padx=15, pady=10)

filler = customtkinter.CTkLabel(master=root, text="                   ")
filler.grid(row=4, column=2)

# buttons (change color on click?)
cbm1 = customtkinter.CTkButton(master=root, text="Deuteranopia", command=colormode_update1, font=("Ariel", 24),
                               height=50, width=150, fg_color='red', hover_color='#A27A01')  # command=cbmode1
cbm1.grid(row=5, column=1, padx=10, pady=10, sticky="ewns")
cbm2 = customtkinter.CTkButton(master=root, text="Protanopia", command=colormode_update2, font=("Ariel", 24), height=50,
                               width=150, fg_color='red', hover_color='#00243d')
cbm2.grid(row=5, column=2, padx=10, pady=10, sticky="ewns")
cbm3 = customtkinter.CTkButton(master=root, text=" Tritanopia ", command=colormode_update3, font=("Ariel", 24),
                               height=50, width=150, fg_color='red', hover_color='#EE3168')
cbm3.grid(row=6, column=1, padx=10, pady=10, sticky="ewns")
cbmd = customtkinter.CTkButton(master=root, text="Default", command=defaultcmode, font=("Ariel", 24), height=50,
                               width=150, fg_color='red', hover_color='#7D7D7D')  # command=defaultcmode
cbmd.grid(row=6, column=2, padx=10, pady=10, sticky="ewns")

# text change slider header
tslabel = customtkinter.CTkLabel(root, text="Text size on graph:", font=("Ariel", 20))
tslabel.grid(row=8, column=0, padx=15)

tsshow = customtkinter.CTkLabel(root, text='20', font=("Ariel", 30))
tsshow.grid(row=8, column=2)


# slider stuf
def slider_event(value):
    tsshow = customtkinter.CTkLabel(root, text=int(value), font=("Ariel", 30))
    # gets value from slider and makes it an int (do the same wherever text size is decided for graphs so you can use slider values)
    tsshow.grid(row=8, column=2)


filler2 = customtkinter.CTkLabel(master=root, text="                   ")
filler2.grid(row=7, column=2)

slider = customtkinter.CTkSlider(master=root, from_=15, to=30, button_color='red', button_hover_color='#7d0000',
                                 command=slider_event)
# lowest txt size: 12, highest: 48, can change if there is a better min/max
slider.grid(row=8, column=1)

credit = customtkinter.CTkLabel(root, text="Built by Millard North Team 1")
credit.grid(row=10, column=1, padx=10, pady=25)

root.mainloop()
