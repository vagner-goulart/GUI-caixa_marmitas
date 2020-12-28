import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)


root_window = Tk()
root_window.geometry("400x400+900+100")

frame_inf_esq = Frame(root_window ,width=200, height=200 ,bg="red", bd=2)

prato_dia = "Arroz, Feijão, Macarrão ao molho vermelho,\nFarofa, Bisteca de porco, Salsicha ao molho.\nFrio: Alface e Tomate."

label_prato_dia = Label(frame_inf_esq, text=prato_dia)
label_prato_dia.grid()

frame_inf_esq.grid()
#frame_inf_esq.grid_propagate(False)
root_window.mainloop()