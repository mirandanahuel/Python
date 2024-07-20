class alumnos:
     tipo="primer año"
     def aula_primer_año(self,fecha_de_incricion,nombre,apellido,edad,año_nacimiento,dni,direccion,email,nacionalidad,telefono):
        cantidad=int(input("ingrese la cantidad de alumnos para incribir  :"))
        for i in range(cantidad+1):
            self.fecha_de_incricion=int(input ("ingrese , fecha"))
            self.nombre=input (f"ingrese ,nombre")
            self.apellido=input (f"ingrese ,apellido")
            self.edad=int (input (f"ingrese, edad"))
            self.año_nacimient=int (input (f"ingrese,fecha de nacimiento"))
            self.dni=int (input (f"ingrese, dni"))
            self.direccion=int (input (f"ingrese ,direccion"))
            self.email=int (input (f"ingrese , email"))
            self.nacionalidad=input (f"ingrese , nacionalidad")
            self.telefono=int (input (f"ingrese,telefono"))
             
print (self.nombre)
