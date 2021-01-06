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

frame_bebidas.check_caixa.load_on_off_images(on_image, off_image)
frame_outros.check_caixa.load_on_off_images(on_image, off_image)

frame_valor_bebidas = FrameDisplayValue(frame_bebidas_outros, "0.00")
frame_valor_bebidas.grid(column=1, pady=(10,0))

# top right corner (parte das marmitas)
frame_marmitas = Frame(root_window, width=250, height=250, bg="#E0E0E0")

marm_pequena = MarmitasFrames(frame_marmitas, 0, "PEQUENA", "marm_pequ")
marm_media = MarmitasFrames(frame_marmitas, 1, "MEDIA", "marm_media")
marm_grande = MarmitasFrames(frame_marmitas, 2, "GRANDE", "marm_grande")

frame_valor_marmitas = FrameDisplayValue(frame_marmitas)
frame_valor_marmitas.grid(pady=(15,0))

# bottom left corner (parte do prato do dia)
frame_dia_ingredientes = Frame(root_window ,width=200, height=200 ,bg="#E0E0E0", bd=2)

dia_semana = "SEGUNDA"
ingredientes_dia = "Arroz, Feijão, Macarrão ao molho vermelho,\nFarofa, Bisteca de porco, Salsicha ao molho.\nFrio: Alface e Tomate."

prato_dia_frame = PratoDiaFrame(frame_dia_ingredientes, dia_semana, ingredientes_dia)

# bottom right corner (parte do pagamento)
pagamento_frame = Frame(root_window, width=300, height=300, bg='red')

total_frame = TrocoFrames(pagamento_frame, "Total")

pagar_com_cartao_checkbox = BaseCheckBox(pagamento_frame)
pagar_com_cartao_checkbox.config(text="Pagar com cartão", font=("SourceSansPro", 15))
pagar_com_cartao_checkbox.grid(sticky=W, padx=(5,0), pady=(10,0))

dinheiro_recebido_frame = TrocoFrames(pagamento_frame, "Input")
troco_do_dinheiro_frame = TrocoFrames(pagamento_frame, "Troco")

# packing the frame with the objects on the screen

# top left (bebidas)
frame_bebidas_outros.grid(row=0, column=0)
frame_marmitas.grid(row=0, column=1)
frame_dia_ingredientes.grid(row=1, column=0)
pagamento_frame.grid(row=1, column=1)

root_window.mainloop()
