import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import FrameDisplayValue, BaseCheckBox
from app_frames import BebidasFrames, MarmitasFrames, PratoDiaFrame, TrocoFrames

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
frame_bebidas = BebidasFrames(frame_bebidas_outros, 0, (10,20), lista_bebidas, "bebidas")

lista_outros = ["Halls", "Trident", "Bala"]
frame_outros = BebidasFrames(frame_bebidas_outros, 1, (20, 10), lista_outros, "outros")

frame_bebidas.check_box.load_on_off_images(on_image, off_image)
frame_outros.check_box.load_on_off_images(on_image, off_image)

frame_valor_bebidas = FrameDisplayValue(frame_bebidas_outros, "0.00")
frame_valor_bebidas.grid(column=1, pady=(10,0))

# top right corner (parte das marmitas)
frame_marmitas = Frame(root_window, width=250, height=250, bg="#E0E0E0")

marm_pequena = MarmitasFrames(frame_marmitas, 0, "PEQUENA", "marm_pequena")
marm_media = MarmitasFrames(frame_marmitas, 1, "MEDIA", "marm_media")
marm_grande = MarmitasFrames(frame_marmitas, 2, "GRANDE", "marm_grande")
tipos_de_marmitas = [marm_pequena, marm_media, marm_grande]

frame_valor_marmitas = FrameDisplayValue(frame_marmitas)
frame_valor_marmitas.grid(pady=(15,0))

# bottom left corner (parte do prato do dia)
frame_dia_ingredientes = Frame(root_window ,width=200, height=200 ,bg="#E0E0E0", bd=2)

dia_semana = "SEGUNDA"
ingredientes_dia = "Arroz, Feijão, Macarrão ao molho vermelho,\nFarofa, Bisteca de porco, Salsicha ao molho.\nFrio: Alface e Tomate."

prato_dia_frame = PratoDiaFrame(frame_dia_ingredientes, dia_semana, ingredientes_dia)

# bottom right corner (parte do pagamento)
pagamento_frame = Frame(root_window, width=300, height=300, bg='gray')

total_frame = TrocoFrames(pagamento_frame, "Total")

pagar_com_cartao_checkbox = BaseCheckBox(pagamento_frame)
pagar_com_cartao_checkbox.config(text="Pagar com cartão", font=("SourceSansPro", 15))
pagar_com_cartao_checkbox.grid(sticky=W, padx=(5,0), pady=(10,0))

dinheiro_recebido_frame = TrocoFrames(pagamento_frame, "Input")
troco_do_dinheiro_frame = TrocoFrames(pagamento_frame, "Troco")

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

    elif char_name == 'Return' and base_str != "000":
        base_str = "000"
    
    dinheiro_recebido_frame.set_value(f"{base_str[:-2]}.{base_str[-2:]}")

dinheiro_recebido_frame.bind('<Key>', update_dinheiro_recebido)
dinheiro_recebido_frame.focus_set()

root_window.mainloop()
