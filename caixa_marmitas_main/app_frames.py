import sys
sys.path.append(".")

from tkinter import *

from my_base_tkinter_objects import (
    BaseCheckBox, BaseDropdownMenu,
    BaseDropdownMenuForQuant, FrameDisplayValue)

import date_and_time as dt

today = dt.get_today_weekday()

class CommonMethodsBebidasMarmitas:
    """Internal class.
    
    This class is for 'BebidasFrames' and 'MarmitasFrames' inheritance only,
    as it only has methods used by them both."""

    def get_quant_menu_var_name(self):
        return str(self.menu_de_quantidade.current_value) # pylint: disable=no-member

    def get_quant_from_quantmenu(self):
        return self.menu_de_quantidade.current_value.get() # pylint: disable=no-member

    def get_checkbox_state(self):
        return self.check_box.get_state() # pylint: disable=no-member

    @property
    def checkbox_is_active(self):
        state = self.get_checkbox_state()
        return state == "sim"

    def link_var_to_frame(self, var):
        self.value_var_to_update = var.value_var

    def add_traces_to_dropdownmenus(self):
        self.menu_de_quantidade.current_value.trace_add('write', self.update_value_label) # pylint: disable=no-member

    def update_value_label(self, v_name=None, *args):
        new_value = self.calculate_new_value(v_name)
        self.value_var_to_update.set(new_value)

    def calculate_new_value(self, v_name):
        current_val = self.value_var_to_update.get()
        quant = self.get_quant_from_quantmenu()
        
        print(f"c_val= {current_val}, ", f"added_value= {self.added_value}") # pylint: disable=access-member-before-definition

        if not self.checkbox_is_active and current_val > 0:
            self.added_value = -(quant*self.preco) # pylint: disable=no-member
        else:
            self.added_value = quant*self.preco # pylint: disable=no-member

        if v_name == self.get_quant_menu_var_name():
            self.added_value -= self.previous_quant*self.preco # pylint: disable=access-member-before-definition, no-member

        self.previous_quant = self.get_quant_from_quantmenu()
        print(f"c_val= {current_val}, ", f"added_value= {self.added_value}")
        # print(v_name)
        # print(self.get_quant_menu_var_name())
        print()

        return self.added_value + current_val


class BebidasFrames(Frame, CommonMethodsBebidasMarmitas):

    def __init__(self, janela, linha, pading, lista_d_items, var_nome, preco, **kwargs):
        super().__init__(janela, bd=1, relief='raised', **kwargs)
        
        self.preco = preco

        self.check_box = BaseCheckBox(self)
        self.check_box.grid(row=linha, column=0)

        self.menu_de_items = BaseDropdownMenu(self, lista_d_items)
        self.menu_de_items.grid(row=linha, column=1, padx=(15,15))

        self.menu_de_quantidade = BaseDropdownMenuForQuant(self, var_nome)
        self.menu_de_quantidade.grid(row=linha, column=2)

        self.grid(pady=pading, columnspan=3)

        self.check_box.check_var.trace_add('write', self.grey_out_elements)

        self.added_value = 0
        self.previous_quant = self.get_quant_from_quantmenu()

    # TODO: esse metodo, assim como o trace_add acima, ta estranho. arruma dps
    def grey_out_elements(self, *args):
        check_buton_state = self.check_box.check_var.get()
        self.update_value_label()

        if check_buton_state == "sim":
            self.menu_de_items.config(state=NORMAL)
            self.menu_de_quantidade.config(state=NORMAL)
        
        else:
            self.menu_de_items.config(state=DISABLED)
            self.menu_de_quantidade.config(state=DISABLED)

    def reset_values(self):
        if self.menu_de_items.get_current_value() != self.menu_de_items.opcoes[0]:
            self.menu_de_items.current_value.set(self.menu_de_items.opcoes[0])
        
        if self.get_quant_from_quantmenu() > 1:
            self.menu_de_quantidade.set_current_value(1)
        
        if self.get_checkbox_state() == "sim":
            self.check_box.deselect()

class MarmitasFrames(Frame, CommonMethodsBebidasMarmitas):

    def __init__(self, janela, linha, nome_marmita, var_nome, preco, **kwargs):
        super().__init__(janela, **kwargs)
        self.config( bd=1, relief='raised')

        self.preco = preco

        self.check_box = BaseCheckBox(self)
        self.check_box.grid(row=linha, column=0)

        self.menu_de_quantidade = BaseDropdownMenuForQuant(self, var_nome)
        self.menu_de_quantidade.grid(row=linha, column=1, padx=(15,10))

        self.label_marmita = Label(
            self,
            text=nome_marmita, font=("SourceSansPro", 11),
            width=10, state=DISABLED)
        self.label_marmita.grid(row=linha, column=2)

        # TODO: this 'if' is kinda garbage, find better solution
        if not "FEIJOADA" in nome_marmita and today == "Saturday":
            self.check_box_feijoada = BaseCheckBox(self, bd=1, relief='raised', state=DISABLED, text="+Feij.")
            self.check_box_feijoada.grid(row=linha, column=3, padx=(10,10))

            self.check_box_feijoada.add_trace(self.add_feijoada_value)

        # TODO: this is totaly temporary, i'll find a better solution
        if not ("FEIJOADA" in nome_marmita and today != "Saturday"):
            self.grid(pady=(20,0))

        self.check_box.check_var.trace_add('write', self.grey_out_elements)

        self.added_value = 0.0
        self.previous_quant = self.get_quant_from_quantmenu()

    # TODO: esse metodo, assim como o trace_add acima, ta estranho. arruma dps
    def grey_out_elements(self, *args):
        check_buton_state = self.check_box.check_var.get()

        self.update_value_label()

        if check_buton_state == "sim":
            self.menu_de_quantidade.config(state=NORMAL, bg='#ccffcc', highlightbackground='#ccffcc')

            self.label_marmita.config(state=NORMAL, bg='#ccffcc')

            if hasattr(self, 'check_box_feijoada'):
                self.check_box_feijoada.config(state=NORMAL, bg='#ccffcc')

            self.config(bg='#ccffcc')
        
        else:
            self.menu_de_quantidade.config(state=DISABLED,bg="#f0f0f0", highlightbackground='#f0f0f0')
            self.label_marmita.config(state=DISABLED,bg="#f0f0f0")

            if hasattr(self, 'check_box_feijoada'):
                self.check_box_feijoada.config(state=DISABLED,bg="#f0f0f0")

            self.config(bg="#f0f0f0")

    def reset_values(self):
        if self.get_checkbox_state() == "nao":
            self.check_box.select()

        if hasattr(self, 'check_box_feijoada') and self.check_box_feijoada.get_state() == "sim":
            self.check_box_feijoada.deselect()

        if self.get_quant_from_quantmenu() > 1:
            self.menu_de_quantidade.current_value.set(1)
        
        self.check_box.deselect()

    def add_feijoada_value(self, *args):
        val = self.get_quant_from_quantmenu() * 2.0

        if self.check_box_feijoada.get_state() == "sim":
            self.preco += 2.0

            self.value_var_to_update.set(self.value_var_to_update.get() + val)
            self.added_value += val
        else:
            self.preco -= 2.0

            self.value_var_to_update.set(self.value_var_to_update.get() - val)
            self.added_value -= val

class PratoDiaFrame(Frame):

    def __init__(self, janela, dia, ingredientes, **kwargs):
        super().__init__(janela, **kwargs)

        self.titulo_dia_semana = "PRATO DO DIA - {}".format(dia)

        self.label_titulo_dia_semana = Label(
            self, text=self.titulo_dia_semana, bg='#E0E0E0', font=("SourceSansPro", 12),)
        self.label_titulo_dia_semana.grid(pady=(10,10))
        
        self.label_prato_dia = Label(self, text=ingredientes, bg='#E0E0E0', font=("SourceSansPro", 11),)
        self.label_prato_dia.grid()

        self.grid()

class TrocoFrames(Frame):

    def __init__(self, janela, texto, **kwargs):
        super().__init__(janela, **kwargs)
        
        self.value = StringVar(value="0.00")

        self.generic_txt_label = Label(self, text=texto+":", width=5, anchor=W, font=("SourceSansPro", 20), bd=2, relief='raised')
        self.generic_txt_label.grid(row=0, column=0)
        
        self.value_label = Label(
            self, textvariable=self.value, bd=2, relief='raised', width=10, anchor=E, font=("SourceSansPro", 20))
        self.value_label.grid(row=0, column=1)

        self.grid(padx=(5,0), pady=(10,0), columnspan=3)

        self.total_value_bebidas = DoubleVar()
        self.total_value_marmitas = DoubleVar()

        self.total_value_bebidas.trace_add('write', self.update_value_var)
        self.total_value_marmitas.trace_add('write', self.update_value_var)

    def add_trace(self, func):
        self.value.trace_add('write', func)

    def get_value(self):
        return self.value.get()

    def set_value(self, val):
        val = self.format_new_value(val)
        self.value.set(val)

    def update_value_var(self, *args):
        new_value = self.total_value_bebidas.get() + self.total_value_marmitas.get()
        new_value = self.format_new_value(new_value)

        self.value.set(new_value)

    @staticmethod
    def format_new_value(value):
        val = str(value)
        splited_val = val.split(".")

        if len(splited_val[-1]) == 1:
            val += "0"

        return val

    def reset_values(self):
        if self.get_value() != "0.00":
            self.set_value(0.00)
