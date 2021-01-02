import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)


class MarmitasFrames(Frame):

    def __init__(self, janela, linha, nome_marmita, **kwargs):
        super().__init__(janela, **kwargs)
        self.config(bg=None, bd=1, relief='raised')

        self.check_box = BaseCheckBox(self)
        self.check_box.grid(row=linha, column=0)

        self.menu_quant = BaseDropdownMenuForQuant(self)
        self.menu_quant.grid(row=linha, column=1, padx=(15,10))

        self.label_marmita = Label(
            self,
            text=nome_marmita, font=("SourceSansPro", 11),
            width=10,)
        self.label_marmita.grid(row=linha, column=2)

        self.grid(pady=(20,0))

        self.check_box.chek_var.trace_add('write', self.grey_out_elements)

    # TODO: esse metodo, assim como o trace_add acima, ta estranho. arruma dps
    def grey_out_elements(self, *args):
        check_buton_state = self.check_box.chek_var.get()

        if check_buton_state == "sim":
            self.menu_quant.config(state=NORMAL)
        
        else:
            self.menu_quant.config(state=DISABLED)

root_window = Tk()
root_window.geometry("400x400+900+100")

frame_marmitas = Frame(root_window, width=250, height=250, bg="#E0E0E0")

marm_pequena = MarmitasFrames(frame_marmitas, 0, "PEQUENA")
marm_media = MarmitasFrames(frame_marmitas, 1, "MEDIA")
marm_grande = MarmitasFrames(frame_marmitas, 2, "GRANDE")


frame_valor = FrameDisplayValue(frame_marmitas)
frame_valor.grid(stick=S, pady=(15,0))

frame_marmitas.grid()
frame_marmitas.grid_propagate(False)
root_window.mainloop()

