import sys
sys.path.append(".")

from tkinter import *
from PIL import ImageTk, Image

from my_base_tkinter_objects import FrameDisplayValue
from app_frames import BebidasFrames

root_window = Tk()
root_window.geometry('600x600+600+50')

# the img being open here is in the same dir as the principal.py file,
# the problem is with vscode that doesn't recognize that. idkw
on_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_on_img.png"))
off_image = ImageTk.PhotoImage(Image.open("caixa_marmitas_main/13x13_off_img.png"))


# creating the top left corner (parte das bebidas)

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

# packing the frame with the objects on the screen
frame_bebidas_outros.grid()

root_window.mainloop()
