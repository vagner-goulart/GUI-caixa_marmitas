from tkinter import *
from PIL import ImageTk, Image


class BaseCheckBox(Checkbutton):

    def __init__(self, janela):
        super().__init__(janela)
        self.chek_var = StringVar()
        self.config(
            bg="green",
            variable=self.chek_var,
            onvalue="sim", offvalue="nao",)

        self.deselect()

    def load_on_off_images(self, on_img, off_img):
        self.config(image=off_img, selectimage=on_img, indicatoron=False,)

class BaseDropdownMenu(OptionMenu):

    def __init__(self, janela, lista_de_opcoes):
        self.current_value = StringVar()
        self.opcoes = lista_de_opcoes
        super().__init__(
            janela, self.current_value,
            *self.opcoes)
        
        self.config(
            width=15,
            font=("SourceSansPro", 13),
            state=DISABLED)

        self.current_value.set(self.opcoes[0])


class BaseDropdownMenuForQuant(OptionMenu):

    def __init__(self, janela):
        self.current_value = IntVar()
        self.quant = [1,2,3,4,5]
        super().__init__(
            janela, self.current_value,
            *self.quant)

        self.config(state=DISABLED)

        self.current_value.set(self.quant[0])


class FrameDisplayValue(Frame):

    def __init__(self, janela, valor=0.00):
        super().__init__(janela, bg=None)

        generic_txt_label = Label(
            self, text="VALOR:", font=("SourceSansPro", 11), bg="#E0E0E0",)
        generic_txt_label.grid(row=0, column=0, stick=E)

        label_valor_3 = Label(
            self,
            text=valor, font=(None, 12),
            borderwidth=1, relief='solid',
            width=8,
            anchor="e")
        label_valor_3.grid(row=0, column=1, padx=(1,1), stick=W)
