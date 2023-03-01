class Usuario:
     #Constructor
     
   def  __init__(self):
        self.__correo = "" 
        self.__password = ""
    
    #Declaramos metodos SETTER y GETTER
        def setCorreo(self,Correo):
            self.__correo=Correo  
        
        def setPassword(self,Password):
            self.__password=Password
        
        def getCorreo(self):
            return self.__correo
        
        def getPassword(self):
            return self.__password    
                