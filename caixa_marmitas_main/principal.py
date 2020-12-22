# estarei usando 'sim' e 'não' para onValue e offValue das checkbox

from tkinter import *

class BaseCheckBox():

    def __init__(self, janela):
        self.chek_var = StringVar()
        self.check_box = Checkbutton(
            janela, bg=None,
            variable=self.chek_var,
            onvalue="sim", offvalue="não")

        self.chek_var.set("nao")

        self.chek_var.trace_add("write", self.printar_teste)

    def printar_teste(self, *args):
        print("slamano")
        print(self.chek_var.get())
        print(args)

class BaseDropdownMenu():

    def __init__(self, janela, lista_de_opcoes):
        self.current_value = StringVar()
        self.opcoes = lista_de_opcoes
        self.dropdown_menu = OptionMenu(
            janela, self.current_value,
            *self.opcoes)
        
        self.dropdown_menu.config(width=15, font=("SourceSansPro", 13))

        self.current_value.set(self.opcoes[0])


class BaseDropdownMenuForQuant():

    def __init__(self, janela):
        self.current_value = IntVar()
        self.quant = [1,2,3,4,5]
        self.dropdown_menu = OptionMenu(
            janela, self.current_value,
            *self.quant)

        self.current_value.set(self.quant[0])


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

