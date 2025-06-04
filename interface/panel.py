from tkinter import Tk, Label, Button

def main_panel(Windows1):
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry("1440x1080")
    Windows.title("Rh_Acesso")
    Windows.iconbitmap("imagens/rh.ico")
    Windows.config(background="white")

    txt_tittle = Label(
        Windows, text="Painel Principal", background="black", font=("Arial", 30)
    )
    txt_tittle.pack(padx=10, pady=10)

    button_image = Button(
        Windows,
        text="Lançar Holerite",
        font=("Arial", 20),
        background="blue",
        fg="white",
        width=20,
    )
    
    button_image.pack(padx=10, pady=50)