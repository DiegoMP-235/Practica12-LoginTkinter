from tkinter import messagebox
class UtileriaLogin:
    def __init__(self):
        self.__activo = True
        
    def validaCamposNoVacios(self,Correo,Password):
        return(Correo != "" and Password != "")

    def compruebaCredenciales(self,Correo,Password,CorreoUser,PasswordUser):
        return (CorreoUser==Correo and PasswordUser==Password)

    def ingresar(self,Correo,Password,CorreoUser,PasswordUser):
        if(self.validaCamposNoVacios(Correo,Password)):
            if(self.compruebaCredenciales(Correo,Password,CorreoUser,PasswordUser)): #En caso de que las credenciales coincidan
                messagebox.showinfo("Inicio exitoso!","Bienvenido al sistema!")
            else: #En caso de que las credenciales no coincidan
                messagebox.showerror("Ha ocurrido un error :/","Las claves de acceso no coinciden")    
        else:
            messagebox.showwarning("Faltan campos","Por favor completa todos los campos")     