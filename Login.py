from Usuario import *
from UtileriaLogin import *
from tkinter import Tk,Frame,Entry,Label,Button,messagebox  
#https://recursospython.com/guias-y-manuales/caja-de-texto-entry-tkinter/
#Para mostrar lo contraseña como oculta
#entrada = Entry(show="*")
def obtenCorreotxt():
    return inputCorreo.get()

def obtenPasswordtxt():
    return inputPassword.get()    
def iniciarSesion():
    inicioSesion.ingresar(obtenCorreotxt(),obtenPasswordtxt(),myUsuer.getCorreo(),myUsuer.getPassword())
    
#Instanciamos objeto tipo Usuario
COLOR="#e0d6bf"
myUsuer = Usuario()
inicioSesion = UtileriaLogin()
CaracterOculto = "■"
#Instanciamos la ventana
ventana = Tk()
ventana.title("Login!")
ventana.geometry("380x250")
ventana.resizable(False,False)

#Instanciamos Frame
Principal = Frame(ventana,bg=COLOR)
Principal.pack(expand=True,fill="both")

#Seccion donde iran etiquetas y entradas de texto
FrameInputs = Frame(Principal,bg=COLOR)
FrameInputs.pack(expand=True,fill="both",pady=20)

#Seccion donde iran los botones
FrameButton = Frame(Principal,bg=COLOR)
FrameButton.pack(expand=True,fill="both")

#Instanciamos entrada de texto y etiquetas
#Campo para el correo
labelCorreo = Label(FrameInputs,text="Correo:")
labelCorreo.place(x=0,y=0,width=75,height=20)

inputCorreo = Entry(FrameInputs,width=35) 
inputCorreo.place(x=85,y=0,width=200,height=20)


#Campo para la password
labelPassword = Label(FrameInputs,text="Contraseña:")
#labelPassword.grid(row = 1,column = 0)
labelPassword.place(x=0,y=40,width=75,height=20)


inputPassword = Entry(FrameInputs,show=CaracterOculto,width=25)
inputPassword.place(x=85,y=40,width=200,height=20)

#Dejamos el correo por defecto para que pueda ingresar
inputCorreo.insert(0,myUsuer.getCorreo())
#Para el boton 
btnIngresar = Button(FrameButton,text="Ingresar",bg="#0dff33",command=iniciarSesion)
btnIngresar.pack()

#mostramos la ventana
ventana.mainloop()