
from tkinter import *
from tkinter import Canvas
from tkinter import ttk


root = Tk()
BG_GREY = '#373737'
BG_BLUE = '#9dbdbc'
BG_YELLOW = '#ffcc66'

# -------------Var
cities = ["Juticalpa", "Arimis"]
sectors = ["1", "2", "3", "4" ]
analysis = ["Landsat", "Cadastro", "Urban Sprawl", "Negative Space", "Roads", "Land Uses"]
FONT_NAME = "Courier"
FONT_SIZE = 14
FONT_TYPE = "normal"
FONT_STYLE = (FONT_NAME, FONT_SIZE, FONT_TYPE)

# -------------------------------- GUI-------------------------
root.title("----Catastro 101----")
root.geometry("672x504")
root.config(bg=BG_GREY)

# ------------------------------Images-------------------------------

canvas = Canvas(width=672, height=504)
# -Base_Map
Map_Base = PhotoImage(file="Maps_Blanck.png")
canvas.create_image(413, 252, image=Map_Base)
canvas.grid(column=1, columnspan=10, row=0)
# - Logo
logo = PhotoImage(file="banner_lateral.png")
canvas.create_image(91, 252, image=logo)
canvas.grid(column=0, row=0, rowspan=5)

# - Combobox City, Sector, Analysis

label_cities = Label(root, text="Cities")
label_cities.config(fg=BG_GREY, font=FONT_STYLE, anchor="w")
label_cities.place(x=20, y=100)
my_combo = ttk.Combobox(root, value=cities)
my_combo.place(x=20, y=130)

label_sectors = Label(root, text="Sector")
label_sectors.config(fg=BG_GREY, font=FONT_STYLE, anchor="w")
label_sectors.place(x=20, y=160)
my_sectors = ttk.Combobox(root, value=sectors)
my_sectors.place(x=20, y=190)

label_sys = Label(root, text="Analysis")
label_sys.config(fg=BG_GREY, font=FONT_STYLE, anchor="w")
label_sys.place(x=20, y=220)
my_sys = ttk.Combobox(root, value=analysis)
my_sys.place(x=20, y=250)




# canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
# pomodo_img = PhotoImage(file="tomato.png")
# canvas.create_image(105, 112, image=pomodo_img)
# canvas.grid(column=1, row=1)




root.mainloop()