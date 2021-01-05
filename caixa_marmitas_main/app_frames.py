import sys
sys.path.append(".")

from tkinter import *

from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)

class BebidasFrames(Frame):

    def __init__(self, janela, linha, pading, lista_d_items, var_nome, **kwargs):
        super().__init__(janela,bg='red', **kwargs)        
        
        self.check_caixa = BaseCheckBox(self)
        self.check_caixa.grid(row=linha, column=0)

        self.menu_de_items = BaseDropdownMenu(self, lista_d_items)
        self.menu_de_items.grid(row=linha, column=1, padx=(25,20))

        self.menu_de_quantidade = BaseDropdownMenuForQuant(self, var_nome)
        self.menu_de_quantidade.grid(row=linha, column=2)

        self.grid(pady=pading, columnspan=3)

        self.check_caixa.chek_var.trace_add('write', self.grey_out_elements)

        self.added_value = 0
        self.previous_quant = self.get_quant_from_quantmenu()

    # TODO: esse metodo, assim como o trace_add acima, ta estranho. arruma dps
    def grey_out_elements(self, *args):
        check_buton_state = self.check_caixa.chek_var.get()
        self.update_value_label()

        if check_buton_state == "sim":
            self.menu_de_items.config(state=NORMAL)
            self.menu_de_quantidade.config(state=NORMAL)
        
        else:
            self.menu_de_items.config(state=DISABLED)
            self.menu_de_quantidade.config(state=DISABLED)


    def get_quant_from_quantmenu(self):
        return self.menu_de_quantidade.current_value.get()
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


class PratoDiaFrame(Frame):

    def __init__(self, janela, dia, ingredientes, **kwargs):
        super().__init__(janela, **kwargs)

        self.titulo_dia_semana = "PRATO DO DIA - {}".format(dia)

        self.label_titulo_dia_semana = Label(
            janela, text=self.titulo_dia_semana, bg='#E0E0E0', font=("SourceSansPro", 12),)
        self.label_titulo_dia_semana.pack(pady=(10,5))
        
        self.label_prato_dia = Label(janela, text=ingredientes, bg='#E0E0E0', font=("SourceSansPro", 11),)
        self.label_prato_dia.pack()


class TrocoFrames(Frame):

    def __init__(self, janela, texto, **kwargs):
        super().__init__(janela, **kwargs)

        self.generic_txt_label = Label(self, text=texto+":", width=5, anchor=W, font=("SourceSansPro", 20))
        self.generic_txt_label.grid(row=0, column=0, sticky=W)
        
        self.value_label = Label(
            self, text="0.00", bd=2, relief='solid', width=10, anchor=E, font=("SourceSansPro", 20))
        self.value_label.grid(row=0, column=1, sticky=W)

        self.grid(sticky=W, padx=(5,0), pady=(10,0))


