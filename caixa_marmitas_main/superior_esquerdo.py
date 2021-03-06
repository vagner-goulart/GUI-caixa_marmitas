# estarei usando 'sim' e 'não' para onValue e offValue das checkbox
import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)


class BebidasFrames(Frame):

    def __init__(self, janela, linha, pading, lista_d_items, **kwargs):
        super().__init__(janela, bg='red', **kwargs)        
        
        self.check_caixa = BaseCheckBox(self)
        self.check_caixa.grid(row=linha, column=0)

        self.menu_de_items = BaseDropdownMenu(self, lista_d_items)
        self.menu_de_items.grid(row=linha, column=1, padx=(25,20))

        self.menu_de_quantidade = BaseDropdownMenuForQuant(self)
        self.menu_de_quantidade.grid(row=linha, column=2)

        self.grid(pady=pading, columnspan=3)

        self.check_caixa.chek_var.trace_add('write', self.grey_out_elements)

    # TODO: esse metodo, assim como o trace_add acima, ta estranho. arruma dps
    def grey_out_elements(self, *args):
        check_buton_state = self.check_caixa.chek_var.get()

        if check_buton_state == "sim":
            self.menu_de_items.config(state=NORMAL)
            self.menu_de_quantidade.config(state=NORMAL)
        
        else:
            self.menu_de_items.config(state=DISABLED)
            self.menu_de_quantidade.config(state=DISABLED)
        

root_window = Tk()
root_window.geometry("400x400")

# the img being open here is in the same dir as the principal.py file,
# the problem is with vscode that doesn't recognize that. idkw
on_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_on_img.png"))
off_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_off_img.png"))

frame_bebidas_outros = Frame(root_window, width=300, height=30)
frame_bebidas_outros.config(bg="blue")

lista_bebidas = ["Água", "CocaCola", "Pepsi"]
frame_bebidas = BebidasFrames(frame_bebidas_outros, 0, (10,20), lista_bebidas)

lista_outros = ["Halls", "Trident", "Bala"]
frame_outros = BebidasFrames(frame_bebidas_outros, 1, (20, 10), lista_outros)

# TODO: find better way off doing this
frame_bebidas.check_caixa.load_on_off_images(on_image, off_image)
frame_outros.check_caixa.load_on_off_images(on_image, off_image)

frame_valor = FrameDisplayValue(frame_bebidas_outros, "0.00")
frame_valor.grid(column=1, pady=(10,0))

frame_bebidas_outros.pack()
frame_bebidas_outros.pack_propagate(False)
root_window.mainloop()
