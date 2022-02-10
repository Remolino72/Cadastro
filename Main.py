import time
from tkinter import *
from tkinter import Canvas
from tkinter import ttk


root = Tk()
BG_GREY = '#373737'
BG_BLUE = '#9dbdbc'
BG_YELLOW = '#ffcc66'

# -------------Var
cities = ["Juticalpa", "Arimis"]
sectors_jut = ["1", "2", "3", "4"]
sectors_ari = ["1", "2"]
analysis = ["Landsat", "Cadastro", "Urban Sprawl", "Negative Space", "Roads", "Land Uses"]
s_img_juti = ["LandSat/JutSector_01.png", "LandSat/JutSector_02.png",
                 "LandSat/JutSector_03.png", "LandSat/JutSector_04.png"]
s_img_ari = ["LandSat/AriSector_01", "LandSat/AriSector_02"]
FONT_NAME = "Courier"
FONT_SIZE = 14
FONT_TYPE = "normal"
FONT_STYLE = (FONT_NAME, FONT_SIZE, FONT_TYPE)
global img_list
img_list = []
#-----------------------------Menu Interaction ----------------------------

def selection(i):
    global img_list
    if my_city.get() == "Juticalpa":
        img_list = s_img_juti
        my_sectors.config(value=sectors_jut)
        map_base.config(file="landSat/JuticalpaSectors.png")

    if my_city.get() == "Arimis":
        img_list = s_img_ari
        my_sectors.config(value=sectors_ari)
        map_base.config(file="landSat/ArimisSectors.png")

def sector_select(n):
    global img_list
    for i in range(len(img_list)+1):
        ii = i - 1
        if i == int(my_sectors.get()):
            print(my_sectors.get())
            map_base.config(file=img_list[ii])
            print(ii)
            continue




# -------------------------------- GUI-------------------------
root.title("----Catastro 101----")
root.geometry("672x504")
root.config(bg=BG_GREY)

# ------------------------------Images-------------------------------

canvas = Canvas(width=672, height=504)
# -Base_Map
m_base = "Maps_Blanck.png"
map_base = PhotoImage(file=m_base)
map_show = canvas.create_image(414, 252, image=map_base)
canvas.grid(column=1, columnspan=10, row=0)

# - Logo
logo = PhotoImage(file="banner_lateral.png")
canvas.create_image(91, 252, image=logo)
canvas.grid(column=0, row=0, rowspan=5)

# ------------- Combobox City, Sector, Analysis------------------------

label_cities = Label(root, text="Cities")
label_cities.config(fg=BG_GREY, font=FONT_STYLE, anchor="w")
label_cities.place(x=20, y=100)
my_city = ttk.Combobox(root, value=cities)
my_city.place(x=20, y=130)
# binding combobox
my_city.bind("<<ComboboxSelected>>", selection)

label_sectors = Label(root, text="Sector")
label_sectors.config(fg=BG_GREY, font=FONT_STYLE, anchor="w")
label_sectors.place(x=20, y=160)
my_sectors = ttk.Combobox(root, value=[""])
my_sectors.place(x=20, y=190)
# bindingbox--------------------
my_sectors.bind("<<ComboboxSelected>>", sector_select)

label_sys = Label(root, text="Analysis")
label_sys.config(fg=BG_GREY, font=FONT_STYLE, anchor="w")
label_sys.place(x=20, y=220)
# my_sys = ttk.Combobox(root, value=[""])
# my_sys.place(x=20, y=250)

# --------------------List boxes-------------------
my_list = Listbox(root, width=23)
my_list.place(x=20, y=250)

# ------------- Buttons ------------------------

enter_button = Button(text="Print", relief=RIDGE, justify=CENTER,

activeforeground="black", width=12, font=FONT_STYLE, bg=BG_BLUE)
enter_button.place(x=20, y=440)



# canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
# pomodo_img = PhotoImage(file="tomato.png")
# canvas.create_image(105, 112, image=pomodo_img)
# canvas.grid(column=1, row=1)




root.mainloop()