from tkinter import Tk, Label, Button

def main_panel(Windows1):
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry("1024x800")
    Windows.title("Principal")
    Windows.config(background="white")

    txt_tittle = Label(
        Windows, text="Painel Principal", background="white", font=("Arial", 30)
    )
    txt_tittle.pack(padx=100, pady=100)

    button_image = Button(
        Windows,
        text="Consultar Salário",
        font=("Arial", 20),
        background="blue",
        fg="white",
        width=20,
    )
    
    button_image.pack(padx=100, pady=50)