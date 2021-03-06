from tkinter import *
from PIL import ImageTk, Image


class BaseCheckBox(Checkbutton):

    def __init__(self, janela=None, **kwargs):
        super().__init__(janela, **kwargs)
        self.check_var = StringVar()
        self.config(
            variable=self.check_var,
            onvalue="sim", offvalue="nao",)

        self.deselect()

    def load_on_off_images(self, on_img, off_img):
        self.config(image=off_img, selectimage=on_img, indicatoron=False,)

    def get_state(self):
        return self.check_var.get()

    def add_trace(self, func):
        self.check_var.trace_add('write', func)

class BaseDropdownMenu(OptionMenu):

    def __init__(self, janela, lista_de_opcoes):
        self.current_value = StringVar()
        self.opcoes = lista_de_opcoes
        
        super().__init__(janela, self.current_value, *self.opcoes)
        
        self.config(
            width=15,
            font=("SourceSansPro", 13),
            state=DISABLED
            )

        self.current_value.set(self.opcoes[0])

    def set_current_value(self, val):
        self.current_value.set(val)

    def get_current_value(self):
        return self.current_value.get()


class BaseDropdownMenuForQuant(OptionMenu):

    def __init__(self, janela, var_nome):
        self.current_value = IntVar(name=var_nome)
        self.quant = [1,2,3,4,5]
        super().__init__(
            janela, self.current_value,
            *self.quant)

        self.config(state=DISABLED)

        self.current_value.set(self.quant[0])

    def set_current_value(self, val):
        self.current_value.set(val)

class FrameDisplayValue(Frame):

    def __init__(self, janela, valor=0.0):
        super().__init__(janela, bg=None)

        self.value_var = DoubleVar(self, value=valor)

        generic_txt_label = Label(
            self, text="VALOR:", font=("SourceSansPro", 11))
        generic_txt_label.grid(row=0, column=0, stick=E)

        self.label_valor_3 = Label(
            self,
            textvariable=self.value_var, font=(None, 12),
            borderwidth=1, relief='solid',
            width=8,
            anchor="e")
        self.label_valor_3.grid(row=0, column=1, padx=(1,1), stick=W)

        self.value_var.trace_add('write', self.update_label_var)

    def create_link_to_label_var(self, var):
        self.total_label_var = var

    def update_label_var(self, *args):
        self.total_label_var.set(self.value_var.get())

