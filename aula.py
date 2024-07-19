class alumnos:

     def aula_primer_año(self,fecha_de_incricion,nombre,apellido,edad,año_nacimiento,dni,direccion,email,nacionalidad,telefono):
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
cantidad=int(input("ingrese lafecha_de_incricion cantidad de alumnos para incribir  :"))
for i in range(0,cantidad,1):
     alumnos.fecha_de_incricion=input(f"fecha de incricion,{i}  :")
     alumnos.nombre=input(f"ingrese su nombre,{i}  :")
     alumnos.apellido=input(f"ingrese,apellido,{i}  :")
     alumnos.edad=input(f"ingrese ,edad,{i} :")
     alumnos.año_nacimiento=input(f"ingrese año de nacimiento,{i}  :")
     alumnos.dni=input(f"ingrese din,{i} :")
     alumnos.direccion=input(f"ingrese direcion,{i}  :")
     alumnos.email=input(f"ingrese,email,{i}  :")
     alumnos.nacionalidad=input(f"ingrese la nacionalidad")
     alumnos.telefono=input(f"ingrese telefono,{i}  :")
opcion=input("mostrar lista de alumnos ,si o no")
if opcion=="si":
     for i in range(cantidad):
          print(f"mostrar,{alumnos.nombre},\n{alumnos.apellido}")
