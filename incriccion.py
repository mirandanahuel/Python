class alumnos:

       def __int__(self,fecha_de_incricion,nombre,apellido,edad,año_nacimiento,dni,direccion,email,nacionalidad,telefono):
          self.fecha_de_incricion
          self.nombre
          self.apellido
          self.edad
          self.año_nacimient
          self.dni
          self.direccion
          self.email
          self.nacionalidad
          self.telefono
      
def validar_dni(alumnos,i):
      alumnos.dni=input(f"ingrese,dni {i} :")
      lon=len(alumnos.dni)
      while lon!=8:
           print("su dni incorrecto ")
           alumnos.dni=input(f"ingrese,dni {i} :")
           lon=len(alumnos.dni)
      if lon==8:
          return alumnos.dni
def validar_telefono(alumnos,i):
      alumnos.telefono=input(f"ingrese,telefono {i} :")
      lon=len(alumnos.telefono)
      while lon!=10:
           alumnos.telefono=input(f"ingrese,telefono {i} :")
           lon=len(alumnos.telefono)
      if lon==10:
           return alumnos.telefono
    
print("opcion:1 , cargar alumnos")
print("opcion:2 ,  ver listado de alumnos")
print("opcion:3 , salir")
menu=int(input("ingrese una opcion "))
while menu!=3:
      if menu==1:
       
           cantidad=int(input("ingrese la cantidad de alumnos para incribir  :"))
           for i in range(1,cantidad+1):
                 alumnos.fecha_de_incricion=input(f"fecha de incricion,{i}  :")
                 alumnos.nombre=input(f"ingrese su nombre,{i}  :")
                 alumnos.apellido=input(f"ingrese,apellido,{i}  :")
                 alumnos.edad=input(f"ingrese ,edad,{i} :")
                 alumnos.año_nacimiento=input(f"ingrese año de nacimiento,{i}  :")
                 alumnos.dni=validar_dni(alumnos,i)
                 alumnos.direccion=input(f"ingrese direcion,{i}  :")
                 alumnos.email=input(f"ingrese,email,{i}  :")
                 alumnos.nacionalidad=input(f"ingrese la nacionalidad")
                 alumnos.telefono=validar_telefono(alumnos,i)
                 print('________________________________________')
                 print("opcion:1 , cargar alumnos")
                 print("opcion:2 ,  ver listado de alumnos")
                 print("opcion:3 , salir")
                 menu=int(input("ingrese una opcion "))             
      if menu==2:    
          opcion=input("mostrar lista de alumnos ,si o no  :")
          if opcion=="si":
               for i in range(cantidad):
   
                    print(f"hola ,{alumnos.nombre},\n{alumnos.apellido},\n{alumnos.edad}\n{alumnos.año_nacimiento}\n{alumnos.dni}\n{alumnos.direccion}\n{alumnos.email}\n{alumnos.nacionalidad}\n{alumnos.telefono}")
          else: 
              print("gracias por elegirnos") 
              print('________________________________________')
              print("opcion:1 , cargar alumnos")
              print("opcion:2 ,  ver listado de alumnos")
              print("opcion:3 , salir")
              menu=int(input("ingrese una opcion "))             

  
         
