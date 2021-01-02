import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)


class TrocoFrames(Frame):

    def __init__(self, janela, texto, **kwargs):
        super().__init__(janela, **kwargs)

        self.generic_txt_label = Label(self, text=texto+":", width=5, anchor=W, font=("SourceSansPro", 20))
        self.generic_txt_label.grid(row=0, column=0, sticky=W)
        
        self.value_label = Label(
            self, text="0.00", bd=2, relief='solid', width=10, anchor=E, font=("SourceSansPro", 20))
        self.value_label.grid(row=0, column=1, sticky=W)

        self.grid(sticky=W, padx=(5,0), pady=(10,0))


root_window = Tk()
root_window.geometry("400x400+900+100")

pagamento_frame = Frame(root_window, width=300, height=300, bg='red')

total_frame = TrocoFrames(pagamento_frame, "Total")

pagar_com_cartao_checkbox = BaseCheckBox(pagamento_frame)
pagar_com_cartao_checkbox.config(text="Pagar com cartão", font=("SourceSansPro", 15))
pagar_com_cartao_checkbox.grid(sticky=W, padx=(5,0), pady=(10,0))

dinheiro_recebido_frame = TrocoFrames(pagamento_frame, "Input")
troco_do_dinheiro_frame = TrocoFrames(pagamento_frame, "Troco")

pagamento_frame.grid()
#pagamento_frame.grid_propagate(False)
root_window.mainloop()