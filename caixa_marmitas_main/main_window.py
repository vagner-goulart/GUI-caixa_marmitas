import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import FrameDisplayValue
from app_frames import BebidasFrames, MarmitasFrames, PratoDiaFrame

root_window = Tk()
root_window.geometry('600x600+600+50')

# the img being open here is in the same dir as the principal.py file,
# the problem is with vscode that doesn't recognize that. idkw
on_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_on_img.png"))
off_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_off_img.png"))


# creating the frames that will go into the main window

# top left corner (parte das bebidas)
frame_bebidas_outros = Frame(root_window, width=300, height=30)
frame_bebidas_outros.config(bg="blue")

lista_bebidas = ["Água", "CocaCola", "Pepsi"]
frame_bebidas = BebidasFrames(frame_bebidas_outros, 0, (10,20), lista_bebidas)

lista_outros = ["Halls", "Trident", "Bala"]
frame_outros = BebidasFrames(frame_bebidas_outros, 1, (20, 10), lista_outros)

frame_bebidas.check_caixa.load_on_off_images(on_image, off_image)
frame_outros.check_caixa.load_on_off_images(on_image, off_image)

frame_valor = FrameDisplayValue(frame_bebidas_outros, "0.00")
frame_valor.grid(column=1, pady=(10,0))

# top right corner (parte das marmitas)
frame_marmitas = Frame(root_window, width=250, height=250, bg="#E0E0E0")

marm_pequena = MarmitasFrames(frame_marmitas, 0, "PEQUENA")
marm_media = MarmitasFrames(frame_marmitas, 1, "MEDIA")
marm_grande = MarmitasFrames(frame_marmitas, 2, "GRANDE")

frame_valor = FrameDisplayValue(frame_marmitas)
frame_valor.grid(pady=(15,0))



# packing the frame with the objects on the screen

# top left (bebidas)
frame_bebidas_outros.grid(row=0, column=0)
frame_marmitas.grid(row=0, column=1)

root_window.mainloop()
