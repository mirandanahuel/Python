#funcion:modificar datos
def modificar(nombre,apellido,edad,fecha,dni,direccion,email,telefono):
	print("bienvenido modificar")
	print("'------------------------------------")
	buscar=input("buscar nombre")
	if buscar==nombre[0]:
		nombre.append(input("modificar"))
	if apellido[0]==nombre[0]:
		print("quiere modificar apellido")
		buscar=input("si o no :")
		if buscar=="si":
			apellido.append(input("apellido:"))
			print("se modifico ")
		else:
			print("no se encotro resultado")
	if edad[0]==nombre[0]:
	  	print("modificar edad")
	  	buscar=input("si o no :")
	  	if buscar=="si":
	  		edad.append(input("edad :"))
	  	else:
	  		print("no se encotro resultado")
	print("gracias por elegirnos")			
#funcion: lista de datos
def lista(nombre,apellido,edad,fecha,dni,direccion,email,telefono):
	print("bienvenido a lista")
	#requiere un for para recorrer lista
	print(nombre[0])
	print(apellido[0])
	print(edad[0])
	print(fecha[0])
	print(dni[0])
	print(direccion[0])
	print(email[0])
	print(telefono[0])
#funcion :baja de datos
def baja(nombre,apellido,edad,fecha,dni,direccion,email,telefono):
	print("bienvenido baja")
	nom=input("baja : nombre")
	if nom==nombre[0]:
		nombre.append("")
		print("nombre se borro")
		if apellido[0]==nombre[0]:
			apellido.append("")
			print("apellido se borro")
			if edad[0]==nombre[0]:
				edad.append("")
				print("edad se borro")
				if fecha[0]==nombre[0]:
					fecha.append("")
					print("fecha se borro")
					if dni[0]==nombre[0]:
						dni.append("")
						print("dni se borro")
#funcion:alta de datos
def alta(nombre,apellido,edad,fecha,dni,direccion,email,telefono):
	print("bienvenido alta")	
	print("--------------------------")
	print("ingrese los datos ")
#requiere un for para almacenar x datos
	nombre.append(input("nombre :"))
	while nombre=="":
		nombre.append(input("nombre"))
	apellido.append(input("apellido :"))
	while apellido=="":
		apellido.append(input("apellido"))
	edad.append(input("edad :"))
	while edad=="":
		edad.append(input("edad"))	
	fecha.append(input("año, nacio:"))
	while fecha=="":
		fecha.append(input("año,nacio"))
	dni.append(input("dni:"))
	while dni=="":
		dni.append(input("dni"))
	direccion.append(input("direccion:"))
	while direccion=="":
		direccion.append(input("direccion"))
	email.append(input("email:"))
	while email=="":
		email.append(input("email"))
	telefono.append(input("telefono"))
	while telefono=="":
		telefono.append(input("telefono"))
		
#funcio:menu
def menu():
	nombre=[]
	apellido=[]
	edad=[]
	fecha=[]
	dni=[]
	direccion=[]
	email=[]
	telefono=[]
	op=1
	while op>=1 and op!=5 and op<=5:
		print("-------MENU,PRINCIPAL-----")
		print("1:altA")
		print("2:baja")
		print("3:lista")
		print("4:moficar")
		print("5:salir")
		print("~~~~~~~~~~~~~~")
		op=int(input("opcion  :"))
		print("~~~~~~~~~~~~~~")
		if op==1:
			alta(nombre,apellido,edad,fecha,dni,direccion,email,telefono)
		elif op==2:
			baja(nombre,apellido,edad,fecha,dni,direccion,email,telefono)
		elif op==3:
			lista(nombre,apellido,edad,fecha,dni,direccion,email,telefono)
		elif op==4:
		 	modificar(nombre,apellido,edad,fecha,dni,direccion,email,telefono)
		else:
		 	print("no se encotro resultado")
#programa pricipal
menu()
