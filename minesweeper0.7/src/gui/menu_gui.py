from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import os

ASSETS_PATH = os.path.abspath("assets/gui_assets/menu")


def start_button():
    subprocess.Popen(["python", os.path.abspath("src/Minesweeper.py")])
    window.quit()


window = Tk()

window.geometry("650x400")
window.configure(bg="#FFFFFF")
window.title("Ana Menü")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=400,
    width=650,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=f"{ASSETS_PATH}/image_1.png")
image_1 = canvas.create_image(393.0, 200.0, image=image_image_1)

canvas.create_text(
    139.0,
    220.0,
    anchor="nw",
    text="Mayın Tarlası",
    fill="#FFFFFF",
    font=("Inter Light", 24 * -1),
)

canvas.create_rectangle(124.5, 256.5, 306.0, 258.0, fill="#FFFFFF", outline="")

button_image_2 = PhotoImage(file=f"{ASSETS_PATH}/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=start_button,
    relief="flat",
)
button_2.place(x=126.0, y=270.0, width=180.0, height=50.0)

canvas.create_text(
    0.0,
    385.0,
    anchor="nw",
    text="Çamoluk Otomotiv™ 2023",
    fill="#FFFFFF",
    font=("Inter SemiBold", 12 * -1),
)
window.resizable(False, False)
window.mainloop()
