# estarei usando 'sim' e 'não' para onValue e offValue das checkbox
import sys
sys.path.append(".")

from tkinter import *
from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)


class Foo():

    def __init__(self, janela, linha, pading, lista_d_items):
        
        this_frame = Frame(janela, bg="red")
        
        
        check_caixa = BaseCheckBox(this_frame)
        check_caixa.check_box.grid(row=linha, column=0)

        menu_de_opcoes_items = BaseDropdownMenu(this_frame, lista_d_items)
        menu_de_opcoes_items.dropdown_menu.grid(row=linha, column=1, padx=(25,20))

        menu_de_quantidade = BaseDropdownMenuForQuant(this_frame)
        menu_de_quantidade.dropdown_menu.grid(row=linha, column=2)


        this_frame.grid(pady=pading, columnspan=3)

root_window = Tk()
root_window.geometry("400x400")

frame_bebidas_outros = Frame(root_window, width=300, height=30)
frame_bebidas_outros.config(bg="blue")

lista_bebidas = ["Água", "CocaCola", "Pepsi"]
frame_bebidas = Foo(frame_bebidas_outros, 0, (10,20), lista_bebidas)

lista_outros = ["Halls", "Trident", "Bala"]
frame_outros = Foo(frame_bebidas_outros, 1, (20, 10), lista_outros)

frame_valor = FrameDisplayValue(frame_bebidas_outros, 20.0)
frame_valor.frame.grid(column=1, pady=(10,0))

frame_bebidas_outros.pack()
frame_bebidas_outros.pack_propagate(False)
root_window.mainloop()

