from Usuario import *
from tkinter import Tk,Frame,Entry,Label,Button,messagebox  
#https://recursospython.com/guias-y-manuales/caja-de-texto-entry-tkinter/
#Para mostrar lo contraseña como oculta
#entrada = Entry(show="*")
def obtenCorreotxt():
    #print(inputCorreo.get())
    return inputCorreo.get()

def obtenPasswordtxt():
    return inputPassword.get()    

def validaCamposNoVacios():
    return(inputCorreo.get() != "" and inputPassword.get() != "")

def compruebaCredenciales(Correo,Password):
    return (myUsuer.getCorreo()==Correo and myUsuer.getPassword()==Password)

def ingresar():
    if(validaCamposNoVacios()):
        if(compruebaCredenciales(obtenCorreotxt(),obtenPasswordtxt())): #En caso de que las credenciales coincidan
            messagebox.showinfo("Inicio exitoso!","Bienvenido al sistema!")
        else: #En caso de que las credenciales no coincidan
            messagebox.showerror("Ha ocurrido un error :/","Las claves de acceso no coinciden")    
    else:
        messagebox.showwarning("Faltan campos","Por favor completa todos los campos")    
    
#Instanciamos objeto tipo Usuario
myUsuer = Usuario()
CaracterOculto = "■"
#Instanciamos la ventana
ventana = Tk()
ventana.title("Login!")
ventana.geometry("380x250")

#Instanciamos Frame
Principal = Frame(ventana,bg="#c8faa5")
Principal.pack(expand=True,fill="both")

#Seccion donde iran etiquetas y entradas de texto
FrameInputs = Frame(Principal,bg="#ada4a3")
FrameInputs.pack(expand=True,fill="both")
#Seccion donde iran los botones
FrameButton = Frame(Principal,bg="#2e60e8")
FrameButton.pack(expand=True,fill="both")

#Instanciamos entrada de texto y etiquetas
#Campo para el correo
labelCorreo = Label(FrameInputs,text="Correo:")
labelCorreo.grid(row = 0,column = 0)

inputCorreo = Entry(FrameInputs,width=35)
inputCorreo.grid(row=0,column=1)

#Campo para la password
labelPassword = Label(FrameInputs,text="Contraseña:")
labelPassword.grid(row = 1,column = 0)

inputPassword = Entry(FrameInputs,show=CaracterOculto,width=25)
inputPassword.grid(row=1,column=1)

#Dejamos el correo por defecto para que pueda ingresar
inputCorreo.insert(0,myUsuer.getCorreo())

#Para el boton 
btnIngresar = Button(FrameButton,text="Ingresar",bg="#0dff21",command=ingresar)
btnIngresar.pack()

#mostramos la ventana
ventana.mainloop()