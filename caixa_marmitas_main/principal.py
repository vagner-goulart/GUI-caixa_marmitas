# estarei usando 'sim' e 'não' para onValue e offValue das checkbox
import sys
sys.path.append(".")

from tkinter import *
from my_base_tkinter_objects import BaseCheckBox, BaseDropdownMenu, BaseDropdownMenuForQuant


class Foo():

    def __init__(self, janela, linha, pading, lista_d_items):
        
        this_frame = Frame(janela, bg="red")
        
        
        check_caixa = BaseCheckBox(this_frame)
        check_caixa.check_box.grid(row=linha, column=0)

        menu_de_opcoes_items = BaseDropdownMenu(this_frame, lista_d_items)
        menu_de_opcoes_items.dropdown_menu.grid(row=linha, column=1, padx=(25,20))

        menu_de_quantidade = BaseDropdownMenuForQuant(this_frame)
        menu_de_quantidade.dropdown_menu.grid(row=linha, column=2)


        this_frame.grid(pady=pading, columnspan=4)

root_window = Tk()
root_window.geometry("400x400")

frame_1 = Frame(root_window, width=300, height=30)
frame_1.config(bg="blue")

lista_bebidas = ["Água", "CocaCola", "Pepsi"]
sla = Foo(frame_1, 0, (10,20), lista_bebidas)

lista_outros = ["Halls", "Trident", "Bala"]
sla_2 = Foo(frame_1, 1, (20, 10), lista_outros)

label_valor_2 = Label(
    frame_1, text="VALOR:",
    font=("SourceSansPro", 10))
label_valor_2.grid(row=2, column=1, stick=E)

label_valor_3 = Label(
    frame_1, text="",
    font=(None, 10))
label_valor_3.grid(row=2, column=2, stick=W)

frame_1.pack()
frame_1.pack_propagate(False)
root_window.mainloop()

