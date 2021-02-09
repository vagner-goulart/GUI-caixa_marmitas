import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import FrameDisplayValue, BaseCheckBox
from app_frames import BebidasFrames, MarmitasFrames, PratoDiaFrame, TrocoFrames

import date_and_time as dt
from ingredientes_marmitas import get_today_ingredients
from pprint import pprint

root_window = Tk()
root_window.geometry('630x450+600+50')

# the img being open here is in the same dir as the main_window.py file,
# the problem is with vscode that doesn't recognize that. idkw
on_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_on_img.png"))
off_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_off_img.png"))

today = dt.get_today_weekday()

# creating the frames that will go into the main window

# top left corner (parte das bebidas)
frame_bebidas_outros = Frame(root_window, width=330, height=200)
frame_bebidas_outros.config(bg='blue', borderwidth=1, relief='solid')
frame_bebidas_outros.columnconfigure(0, weight=1)

lista_bebidas = ["Água", "CocaCola", "Pepsi"]
frame_bebidas_um = BebidasFrames(frame_bebidas_outros, 0, (10,10), lista_bebidas, "bebidas_um", 5.0)

frame_bebidas_dois = BebidasFrames(frame_bebidas_outros, 1, (10,0), lista_bebidas, "bebidas_dois", 5.0)

lista_outros = ["Halls", "Trident", "Bala"]
frame_outros = BebidasFrames(frame_bebidas_outros, 2, (20, 10), lista_outros, "outros", 5.0)

frame_bebidas_um.check_box.load_on_off_images(on_image, off_image)
frame_bebidas_dois.check_box.load_on_off_images(on_image, off_image)
frame_outros.check_box.load_on_off_images(on_image, off_image)

frame_valor_bebidas = FrameDisplayValue(frame_bebidas_outros, "0.0")
frame_valor_bebidas.grid(pady=(10,0))

# top right corner (parte das marmitas)
frame_marmitas = Frame(root_window, width=300, height=200, bg="green", borderwidth=1, relief='solid')
frame_marmitas.columnconfigure(0, weight=1)

marm_pequena = MarmitasFrames(frame_marmitas, 0, "PEQUENA", "marm_pequena", 5.0)
marm_media = MarmitasFrames(frame_marmitas, 1, "MEDIA", "marm_media", 5.0)
marm_grande = MarmitasFrames(frame_marmitas, 2, "GRANDE", "marm_grande", 5.0)
tipos_de_marmitas = [marm_pequena, marm_media, marm_grande]

frame_valor_marmitas = FrameDisplayValue(frame_marmitas)
frame_valor_marmitas.grid(pady=(15,0))

for marm in tipos_de_marmitas:
    marm.check_box.load_on_off_images(on_image, off_image)

# bottom left corner (parte do prato do dia)
frame_dia_ingredientes = Frame(root_window ,width=330, height=250 ,bg="green", borderwidth=1, relief='solid')
frame_dia_ingredientes.columnconfigure(0, weight=1)

dia_semana = dt.get_today_weekday_in_PT()
ingredientes_dia = get_today_ingredients()

prato_dia_frame = PratoDiaFrame(frame_dia_ingredientes, dia_semana, ingredientes_dia)

marm_feijoada.check_box.load_on_off_images(on_image, off_image)

marm_feijoada.link_var_to_frame(frame_valor_marmitas)
marm_feijoada.add_traces_to_dropdownmenus()

# bottom right corner (parte do pagamento)
pagamento_frame = Frame(root_window, width=300, height=250, bg='yellow', borderwidth=1, relief='solid')
pagamento_frame.columnconfigure(0, weight=1)

total_frame = TrocoFrames(pagamento_frame, "Total")

pagar_com_cartao_checkbox = BaseCheckBox(pagamento_frame)
pagar_com_cartao_checkbox.config(text="Pagar com cartão", font=("SourceSansPro", 15), state=DISABLED)
pagar_com_cartao_checkbox.grid(padx=(5,0), pady=(10,0), columnspan=3)

dinheiro_recebido_frame = TrocoFrames(pagamento_frame, "Input")
troco_do_dinheiro_frame = TrocoFrames(pagamento_frame, "Troco")

botoes_frame = Frame(pagamento_frame, bg='light gray')

botao_terminar = Button(botoes_frame, text="Terminar", font=("SourceSansPro", 12), state=DISABLED)
botao_cancelar = Button(botoes_frame, text="Cancelar", font=("SourceSansPro", 12))
botoes_lista = [botao_cancelar, botao_cancelar]

botao_cancelar.grid(row=0, column=0)
botao_terminar.grid(row=0, column=1, padx=(10, 0))

botoes_frame.grid(pady=(10,0))

# packing the frame with the objects on the screen
frame_bebidas_outros.grid(row=0, column=0)
frame_marmitas.grid(row=0, column=1)
frame_dia_ingredientes.grid(row=1, column=0)
pagamento_frame.grid(row=1, column=1)

# TODO: this is kinda bad. fix later
for frame in [frame_bebidas_outros, frame_marmitas, frame_dia_ingredientes, pagamento_frame]:
    frame.grid_propagate(False)

frame_bebidas_um.link_var_to_frame(frame_valor_bebidas)
frame_bebidas_um.add_traces_to_dropdownmenus()

frame_bebidas_dois.link_var_to_frame(frame_valor_bebidas)
frame_bebidas_dois.add_traces_to_dropdownmenus()

frame_outros.link_var_to_frame(frame_valor_bebidas)
frame_outros.add_traces_to_dropdownmenus()

for marmita in tipos_de_marmitas:
    marmita.link_var_to_frame(frame_valor_marmitas)
    marmita.add_traces_to_dropdownmenus()

frame_valor_bebidas.create_link_to_label_var(total_frame.total_value_bebidas)
frame_valor_marmitas.create_link_to_label_var(total_frame.total_value_marmitas)

dinheiro_faltando_label = Label(dinheiro_recebido_frame, bg="white", text="Quantia Insuficiente!", fg='red')

# TODO: move all functions to the top of the file
def update_dinheiro_recebido(event):
    
    base_str = dinheiro_recebido_frame.get_value()
    base_str = base_str.replace(".", "")
    
    char = event.char
    char_name = event.keysym

    if char_name == 'BackSpace':
        only_have_zeros = len(set(base_str)) == 1 and "0" in set(base_str)
        
        if not only_have_zeros:
            base_str = base_str[:-1]
            
            if len(base_str) == 2:
                base_str = "0" + base_str

    elif char_name.isdigit() and len(base_str) < 9:
        if base_str[0] == "0":
            base_str = base_str[1:]
            base_str += char
        else:
            base_str += char

    # TODO: this 'elif' is too long and hard to understand
    elif char_name == 'Return' and base_str != "000" and total_frame.get_value() != "0.00":

        total = float(total_frame.get_value())
        dinheiro_recebido = float(f"{base_str[:-2]}.{base_str[-2:]}")
        troco = dinheiro_recebido - total
    
        if troco < 0:
            #this will grid the label in the screen if it isn't already there
            if dinheiro_faltando_label.winfo_manager() == "":
                dinheiro_faltando_label.grid(column=1, sticky='e')

            #this will grayout the 'terminar' button if it is visible
            if botao_terminar.cget('state') == 'normal':
                botao_terminar.config(state=DISABLED)
            if botao_terminar.cget('bg') == 'lime':
                botao_terminar.config(bg='#F0F0F0')

            #this will change the value of 'troco' frame to "0.00" if it's diferent than "0.00"
            if troco_do_dinheiro_frame.get_value() != "0.00":
                troco_do_dinheiro_frame.set_value("0.00")
        else:
            troco_do_dinheiro_frame.set_value(round(troco, 2))
            
            #this will make the 'terminar' button clikcable and the 'cancelar' button red(ish)
            botao_terminar.config(bg='lime', state=NORMAL)
            botao_cancelar.config(bg='#ff3333')

            #this will remove the label if it is on the screen
            if dinheiro_faltando_label.winfo_manager() == 'grid':
                dinheiro_faltando_label.grid_remove()
    
    #new_val = f"{base_str[:-2]}.{base_str[-2:]}"
    new_val = "{all_digits_but_the_last_two}.{last_two_digits}".format(
        all_digits_but_the_last_two=base_str[:-2],
        last_two_digits=base_str[-2:]
    )
    dinheiro_recebido_frame.set_value(new_val)

def reset_all_values(event=None):
    pagar_com_cartao_checkbox.check_var.set("nao")

    frame_bebidas_um.reset_values()
    frame_bebidas_dois.reset_values()
    frame_outros.reset_values()

    marm_pequena.reset_values()
    marm_media.reset_values()
    marm_grande.reset_values()

    marm_feijoada.reset_values()

    total_frame.reset_values()
    dinheiro_recebido_frame.reset_values()
    troco_do_dinheiro_frame.reset_values()

    if dinheiro_faltando_label.winfo_manager() == 'grid':
        dinheiro_faltando_label.grid_remove()

    botao_cancelar.config(bg='#F0F0F0')
    botao_terminar.config(bg='#F0F0F0', state=DISABLED)

def pagar_com_cartao(*args):
    usar_cartao = pagar_com_cartao_checkbox.get_state() == "sim"
    valor_maior_que_zero = float(total_frame.get_value()) > 0.0
    
    if valor_maior_que_zero:
        if usar_cartao:
            dinheiro_recebido_frame.unbind('<Key>')
            dinheiro_recebido_frame.set_value(total_frame.get_value())

            troco_do_dinheiro_frame.set_value("0.00")

            botao_terminar.config(bg='lime', state=NORMAL)
            botao_cancelar.config(bg='#ff3333')
        elif not usar_cartao:
            dinheiro_recebido_frame.bind('<Key>', update_dinheiro_recebido)
            dinheiro_recebido_frame.set_value("0.00")

            botao_terminar.config(bg='#F0F0F0', state=DISABLED)
            botao_cancelar.config(bg='#F0F0F0')

def grey_out_checkbox_pagar_com_cartao(*args):
    val = float(total_frame.get_value())

    if val > 0.0 and pagar_com_cartao_checkbox.cget('state') == 'disabled':
        pagar_com_cartao_checkbox.config(state=NORMAL)
    elif val == 0.0:
        if pagar_com_cartao_checkbox.get_state() == "sim":
            pagar_com_cartao_checkbox.deselect()
            dinheiro_recebido_frame.set_value("0.00")

        pagar_com_cartao_checkbox.config(state=DISABLED)

def coletar_iformacoes_da_venda(*args):
    produtos_vendidos = {
        "Bebidas":{
            "bebidas_um":None,
            "bebidas_dois":None,
        },
        "Outros":None,
        "Marmitas":{
            "Pequena":None,
            "Media":None,
            "Grande":None
        },
        "Feijoada":None
    }


    vendeu_bebida = (
        frame_bebidas_um.get_checkbox_state() == "sim" or
        frame_bebidas_dois.get_checkbox_state() == "sim"
    )
    vendeu_outro = frame_outros.get_checkbox_state() == "sim"

    vendeu_marmita_pequena = marm_pequena.get_checkbox_state() == "sim"
    vendeu_marmita_media   = marm_media.get_checkbox_state() == "sim"
    vendeu_marmita_grande  = marm_grande.get_checkbox_state() == "sim"
    vendeu_marmita = vendeu_marmita_pequena or vendeu_marmita_media or vendeu_marmita_grande

    marmitas_info = {
        # TODO: "Pequena":{"object_address":marm_pequena, "sold_bool":vendeu_marmita_pequena} do something like this later
        "Pequena":[marm_pequena, vendeu_marmita_pequena],
        "Media":[marm_media, vendeu_marmita_media],
        "Grande":[marm_grande, vendeu_marmita_grande]
    }

    vendeu_feijoada = marm_feijoada.get_checkbox_state() == "sim"

    if vendeu_bebida:

        if frame_bebidas_um.get_checkbox_state() == "sim":
            vendido = dict(
                quantidade=frame_bebidas_um.get_quant_from_quantmenu(),
                item=frame_bebidas_um.menu_de_items.current_value.get()
            )

            produtos_vendidos["Bebidas"]["bebidas_um"] = vendido

        if frame_bebidas_dois.get_checkbox_state() == "sim":
            vendido = dict(
                quantidade=frame_bebidas_dois.get_quant_from_quantmenu(),
                item=frame_bebidas_dois.menu_de_items.current_value.get()
            )

            produtos_vendidos["Bebidas"]["bebidas_dois"] = vendido

    if vendeu_outro:
        vendido = dict(
            item=frame_outros.menu_de_items.current_value.get(),
            quantidade=frame_outros.get_quant_from_quantmenu()
            )

        produtos_vendidos["Outros"] = vendido

    if vendeu_marmita:

        for marmita_info in marmitas_info.items():
            tipo_marmita   = marmita_info[0]
            marmita_object = marmita_info[1][0]
            vendeu_marmita = marmita_info[1][1]
            
            if vendeu_marmita:
                if hasattr(marmita_object, 'check_box_feijoada'):
                    feij = marmita_object.check_box_feijoada.get_state()
                else:
                    feij = None

                vendido = dict(
                    quantidade=marmita_object.get_quant_from_quantmenu(),
                    feijoada=feij
                    )
                
                produtos_vendidos["Marmitas"][tipo_marmita] = vendido

    if vendeu_feijoada:
        vendido = dict(
            quantidade=marm_feijoada.get_quant_from_quantmenu()
        )

        produtos_vendidos["Feijoada"] = vendido

    vendas_info = {
        "Vendas":produtos_vendidos,
        "Dia_da_semana":dt.get_today_weekday(),
        "Data":dt.get_today_date(),
        "Horario":dt.get_current_time()
    }

    reset_all_values()

total_frame.add_trace(grey_out_checkbox_pagar_com_cartao)

# TODO: find better solution and move this up close to the checkbox creation
pagar_com_cartao_checkbox.add_trace(pagar_com_cartao)

dinheiro_recebido_frame.bind('<Key>', update_dinheiro_recebido)
dinheiro_recebido_frame.focus_set()

botao_cancelar.config(command=reset_all_values)
botao_terminar.config(command=coletar_iformacoes_da_venda)

root_window.mainloop()
