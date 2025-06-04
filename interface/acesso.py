from tkinter import Tk, Label, Button, Entry
import panel

def screen():
    Windows = Tk()
    Windows.geometry("1024x800")
    Windows.title("Cadastro de Colaborador")
    Windows.config(background="white")

    txt_title = Label(Windows, text="Administração de Colaboradores", background="white",font=("Arial", 20, "bold"))
    txt_title.pack(padx=100, pady=100)

    txt_logout_login = Label(Windows, text= "Usuário", background="white",font=("Arial", 20))
    txt_logout_login.pack(padx=10, pady=10)

    entry_box_login = Entry(Windows, font=("Arial", 15), border="1.5px",background="white")
    entry_box_login.pack(padx=10, pady=10)

    txt_logout_password = Label(Windows, text= "Senha", background="white",font=("Arial", 20))
    txt_logout_password.pack(padx=10, pady=10)

    entry_box_password = Entry(Windows, font=("Arial", 15), border="1.5px",background="white")
    entry_box_password.pack(padx=10, pady=10)

    button_logout = Button(Windows, text="Entrar", font=[16], background="blue", fg="white", width=20)
    button_logout[
        "command"
    ] = lambda button_logout=button_logout: open_panel_one(Windows)
    button_logout.pack(padx=10, pady=50)

    def open_panel_one(self):
        panel.main_panel(self)

    Windows.mainloop()
screen()