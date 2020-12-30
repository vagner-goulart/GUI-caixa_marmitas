import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)


class PratoDiaFrame(Frame):

    def __init__(self, janela, dia, ingredientes, **kwargs):
        super().__init__(janela, **kwargs)

        self.titulo_dia_semana = "PRATO DO DIA - {}".format(dia)

        self.label_titulo_dia_semana = Label(
            janela, text=self.titulo_dia_semana, bg='#E0E0E0', font=("SourceSansPro", 12),)
        self.label_titulo_dia_semana.pack(pady=(10,5))
        
        self.label_prato_dia = Label(janela, text=ingredientes, bg='#E0E0E0', font=("SourceSansPro", 11),)
        self.label_prato_dia.pack()


root_window = Tk()
root_window.geometry("400x400+900+100")

frame_inf_esq = Frame(root_window ,width=200, height=200 ,bg="#E0E0E0", bd=2)

dia_semana = "SEGUNDA"

ingredientes_dia = "Arroz, Feijão, Macarrão ao molho vermelho,\nFarofa, Bisteca de porco, Salsicha ao molho.\nFrio: Alface e Tomate."

prato_dia_frame = PratoDiaFrame(frame_inf_esq, dia_semana, ingredientes_dia)

frame_inf_esq.grid()
#frame_inf_esq.grid_propagate(False)
root_window.mainloop()