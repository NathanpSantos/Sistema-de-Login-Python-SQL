from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

# Criar Nossa Janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
#jan.iconbitmap(default="icon/LogoIcon.ico")#

# Carregando Imagens
logo = PhotoImage(file="logo.png")

# Widgets
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    conn, cursor = database.connect()
    cursor.execute("""
    SELECT * FROM Users
    WHERE User = ? and Password = ?
    """, (User, Pass))
    VerifyLogin = cursor.fetchone()
    database.close(conn)

    if VerifyLogin:
        if User == VerifyLogin[3] and Pass == VerifyLogin[4]:
            messagebox.showinfo(title="Login Info", message="Acesso confirmado. Bem Vindo!")
        else:
            messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se está cadastrado")
    else:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se está cadastrado")

# Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    # Removendo widgets de Login
    LoginButton.place(x=8000)
    RegisterButton.place(x=8000)

    # Adicionando widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = Entry(RightFrame, width=41)
    NomeEntry.place(x=90, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=50)

    EmailEntry = Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if Name == "" or Email == "" or User == "" or Pass == "":
            messagebox.showerror(title="Register Error", message="Preencha todos os campos")
        else:
            conn, cursor = database.connect()
            cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            conn.commit()
            database.close(conn)
            messagebox.showinfo(title="Register Info", message="Cadastro realizado com sucesso!")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        # Removendo widgets de Cadastro
        NomeLabel.place(x=8000)
        NomeEntry.place(x=8000)
        EmailLabel.place(x=8000)
        EmailEntry.place(x=8000)
        Register.place(x=8000)
        Back.place(x=8000)
        # Trazendo de volta os widgets de Login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="Register", width=30, command=Register)
RegisterButton.place(x=100, y=260)

jan.mainloop()
