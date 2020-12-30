import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)


root_window = Tk()
root_window.geometry("400x400+900+100")

frame_inf_esq = Frame(root_window ,width=200, height=200 ,bg="#E0E0E0", bd=2)

titulo_dia_semana = "PRATO DO DIA - {}".format("SEGUNDA")
label_titulo_dia_semana = Label(frame_inf_esq, text=titulo_dia_semana, bg='#E0E0E0', font=("SourceSansPro", 12),)
label_titulo_dia_semana.pack(pady=(10,5))

prato_dia = "Arroz, Feijão, Macarrão ao molho vermelho,\nFarofa, Bisteca de porco, Salsicha ao molho.\nFrio: Alface e Tomate."
label_prato_dia = Label(frame_inf_esq, text=prato_dia, bg='#E0E0E0', font=("SourceSansPro", 11),)
label_prato_dia.pack()

frame_inf_esq.grid()
#frame_inf_esq.grid_propagate(False)
root_window.mainloop()