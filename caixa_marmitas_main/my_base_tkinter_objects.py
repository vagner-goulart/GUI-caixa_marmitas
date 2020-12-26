from tkinter import *


class BaseCheckBox():

    def __init__(self, janela):
        self.chek_var = StringVar()
        self.check_box = Checkbutton(
            janela, bg="green",
            variable=self.chek_var,
            onvalue="sim", offvalue="nao",)

        self.chek_var.set("nao")

class BaseDropdownMenu():

    def __init__(self, janela, lista_de_opcoes):
        self.current_value = StringVar()
        self.opcoes = lista_de_opcoes
        self.dropdown_menu = OptionMenu(
            janela, self.current_value,
            *self.opcoes)
        
        self.dropdown_menu.config(
            width=15,
            font=("SourceSansPro", 13),
            state=DISABLED)

        self.current_value.set(self.opcoes[0])


class BaseDropdownMenuForQuant():

    def __init__(self, janela):
        self.current_value = IntVar()
        self.quant = [1,2,3,4,5]
        self.dropdown_menu = OptionMenu(
            janela, self.current_value,
            *self.quant)

        self.dropdown_menu.config(state=DISABLED)

        self.current_value.set(self.quant[0])


class FrameDisplayValue():

    def __init__(self, janela, valor=0.0):

        self.frame = Frame(janela, bg=None)

        generic_txt_label = Label(
            self.frame, text="VALOR:",
            font=("SourceSansPro", 11))
        generic_txt_label.grid(row=0, column=0, stick=E)

        label_valor_3 = Label(
            self.frame,
            text=valor,
            font=(None, 11),
            width=8,
            borderwidth=1,
            relief='solid',
            anchor="e")
        label_valor_3.grid(row=0, column=1, padx=(1,1), stick=W)
