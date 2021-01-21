import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import FrameDisplayValue, BaseCheckBox
from app_frames import BebidasFrames, MarmitasFrames, PratoDiaFrame, TrocoFrames

from pprint import pprint

root_window = Tk()
root_window.geometry('600x600+600+50')

# the img being open here is in the same dir as the main_window.py file,
# the problem is with vscode that doesn't recognize that. idkw
on_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_on_img.png"))
off_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_off_img.png"))


# creating the frames that will go into the main window

# top left corner (parte das bebidas)
frame_bebidas_outros = Frame(root_window, width=300, height=30)
frame_bebidas_outros.config(bg="blue")

lista_bebidas = ["Água", "CocaCola", "Pepsi"]
frame_bebidas = BebidasFrames(frame_bebidas_outros, 0, (10,20), lista_bebidas, "bebidas", 5.0)

lista_outros = ["Halls", "Trident", "Bala"]
frame_outros = BebidasFrames(frame_bebidas_outros, 1, (20, 10), lista_outros, "outros", 5.0)

frame_bebidas.check_box.load_on_off_images(on_image, off_image)
frame_outros.check_box.load_on_off_images(on_image, off_image)

frame_valor_bebidas = FrameDisplayValue(frame_bebidas_outros, "0.00")
frame_valor_bebidas.grid(column=1, pady=(10,0))

# top right corner (parte das marmitas)
frame_marmitas = Frame(root_window, width=250, height=250, bg="#E0E0E0")

marm_pequena = MarmitasFrames(frame_marmitas, 0, "PEQUENA", "marm_pequena", 5.0)
marm_media = MarmitasFrames(frame_marmitas, 1, "MEDIA", "marm_media", 5.0)
marm_grande = MarmitasFrames(frame_marmitas, 2, "GRANDE", "marm_grande", 5.0)
tipos_de_marmitas = [marm_pequena, marm_media, marm_grande]

frame_valor_marmitas = FrameDisplayValue(frame_marmitas)
frame_valor_marmitas.grid(pady=(15,0))

# bottom left corner (parte do prato do dia)
frame_dia_ingredientes = Frame(root_window ,width=200, height=200 ,bg="#E0E0E0", bd=2)

dia_semana = "SEGUNDA"
ingredientes_dia = "Arroz, Feijão, Macarrão ao molho vermelho,\nFarofa, Bisteca de porco, Salsicha ao molho.\nFrio: Alface e Tomate."

prato_dia_frame = PratoDiaFrame(frame_dia_ingredientes, dia_semana, ingredientes_dia)

marm_feijoada = MarmitasFrames(frame_dia_ingredientes, 1, "FEIJOADA", "feijoada", 30.0)

marm_feijoada.link_var_to_frame(frame_valor_marmitas)
marm_feijoada.add_traces_to_dropdownmenus()

# bottom right corner (parte do pagamento)
pagamento_frame = Frame(root_window, width=300, height=300, bg='gray')

total_frame = TrocoFrames(pagamento_frame, "Total")

pagar_com_cartao_checkbox = BaseCheckBox(pagamento_frame)
pagar_com_cartao_checkbox.config(text="Pagar com cartão", font=("SourceSansPro", 15), state=DISABLED)
pagar_com_cartao_checkbox.grid(sticky=W, padx=(5,0), pady=(10,0), columnspan=3)

dinheiro_recebido_frame = TrocoFrames(pagamento_frame, "Input")
troco_do_dinheiro_frame = TrocoFrames(pagamento_frame, "Troco")

botoes_frame = Frame(pagamento_frame, bg='light gray')

botao_terminar = Button(botoes_frame, text="Terminar", font=("SourceSansPro", 12), state=DISABLED)
botao_cancelar = Button(botoes_frame, text="Cancelar", font=("SourceSansPro", 12))
botoes_lista = [botao_cancelar, botao_cancelar]

botao_cancelar.grid(row=0, column=0)
botao_terminar.grid(row=0, column=1, padx=(10, 0))

botoes_frame.grid(columnspan=3, pady=(10,0))

# packing the frame with the objects on the screen
frame_bebidas_outros.grid(row=0, column=0)
frame_marmitas.grid(row=0, column=1)
frame_dia_ingredientes.grid(row=1, column=0)
pagamento_frame.grid(row=1, column=1)

frame_bebidas.link_var_to_frame(frame_valor_bebidas)
frame_bebidas.add_traces_to_dropdownmenus()
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

    frame_bebidas.reset_values()
    frame_outros.reset_values()

    marm_pequena.reset_values()
    marm_media.reset_values()
    marm_grande.reset_values()

    marm_feijoada.reset_values()

    total_frame.reset_values()
    dinheiro_recebido_frame.reset_values()
    troco_do_dinheiro_frame.reset_values()

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

total_frame.add_trace(grey_out_checkbox_pagar_com_cartao)

# TODO: find better solution and move this up close to the checkbox creation
pagar_com_cartao_checkbox.add_trace(pagar_com_cartao)

dinheiro_recebido_frame.bind('<Key>', update_dinheiro_recebido)
dinheiro_recebido_frame.focus_set()

botao_cancelar.bind('<Button-1>', reset_all_values)

root_window.mainloop()
