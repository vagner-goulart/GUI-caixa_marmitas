import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)


class BuildBarObject(Frame):

    def __init__(self, janela, texto, **kwargs):
        super().__init__(janela, **kwargs)

        generic_txt_label = Label(self, text=texto+":", width=5, anchor=W, font=("SourceSansPro", 20))
        generic_txt_label.grid(row=0, column=0, sticky=W)
        
        value_label = Label(self, text="0.00", bd=2, relief='solid', width=10, anchor=E, font=("SourceSansPro", 20))
        value_label.grid(row=0, column=1, sticky=W)

        self.grid(sticky=W, padx=(5,0), pady=(10,0))


root_window = Tk()
root_window.geometry("400x400+900+100")

sla_frame = Frame(root_window, width=300, height=300, bg='red')

test = BuildBarObject(sla_frame, "Total")

check_sla = BaseCheckBox(sla_frame)
check_sla.config(text="Pagar com cartão", font=("SourceSansPro", 15))
check_sla.grid(sticky=W, padx=(5,0), pady=(10,0))

test_1 = BuildBarObject(sla_frame, "Input")
test_2 = BuildBarObject(sla_frame, "Troco")

sla_frame.grid()
#sla_frame.grid_propagate(False)
root_window.mainloop()