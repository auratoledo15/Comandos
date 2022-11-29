import csv

def leer_csv(ruta):
    ubicacion_csv = ruta
    with open(ubicacion_csv, 'r', newline = '') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            print(row)
            
def crear_csv(lista_datos, ruta):
    ubicacion_csv = ruta
    with open(ubicacion_csv, 'w', newline = '')as csvfile:
        writer = csv.writer(csvfile, delimiter = ';')
        writer.writerows(lista_datos)

def agregar_csv(ruta, lista):
    ubicacion_csv = ruta
    with open(ubicacion_csv, 'r', newline = '')as csvfile:
         reader = csv.reader(csvfile, delimiter=';')
         data = [line for line in reader]
         with open(ubicacion_csv, 'w', newline = '')as csvfile:
             lista_datos2 = lista
             writer = csv.writer(csvfile, delimiter = ';')
             writer.writerows(data)
             writer.writerows(lista_datos2)

def eliminar_csv(search, ruta):
    ubicacion_csv = ruta
    with open(ubicacion_csv, 'r', newline = '')as csvfile:
         reader = csv.reader(csvfile, delimiter=';')
         data = [line for line in reader]
         with open(ubicacion_csv, 'w', newline = '')as csvfile:
              writer = csv.writer(csvfile, delimiter = ';')
              data.pop(search)
              writer.writerows(data)
              
def llenar (lista,cnt_personas):
    for i in range(cnt_personas):
        lista.append([])
        for j in range(3):
            dato=str(input("Digite el "+lista[0][j]+" de la persona: "))
            lista[i+1].append(dato)
            
lista=[['id','nombre','apellido']]
'cnt_personas=int(input("Digite la cantidad de personas a registrar: "))'
'llenar(lista,cnt_personas)'
print(lista)

'lista_datos = [["id", "nombre", "apellido"],["1", "carlos", "rodriguez"],["2", "jose", "benitez"]]'
'crear_csv(lista)'
'leer_csv()'

x = 0

while (x != 5):
    lista = [['id', 'nombre', 'apellido']]
    print("---------------------------------------------------------------------------")
    print("selecione una opcion...")
    print("\t1 - crear archivo csv")
    print("\t2 - leer archivo csv")
    print("\t3 - actuaizar archivo csv")
    print("\t4 - busar y eliminar un dato dentro de un archivo csv")
    print("\t5 - salir")

    x = (int(input(" escoger opcion :")))

    if (x == 1):

        y = 1

        while (y != 0):

            y = (int(input("\n SubMenu\n bienvenido al Submenu \n Opcion 1: Llenar lista por teclado \n Opcion 2: Leer lista a guardar en archivo Csv \n Opcion 0: Salir al menu principal \n Opcion a escoger:")))

            if (y == 1):
                cnt_personas = int(input("ingresar la cantidad de personas a registrar: "))
                llenar(lista, cnt_personas)
            if(y==2):
                print(lista)
                t=str(input("deseas guardar el archivo como csv: s=si n=no "))
                if(t=="s"):
                    ruta=str(input("ingresar donde se va a guardar el archivo: "))
                    nombre=str(input("ingresarel nombre del archivo: "))
                    crear_csv(lista, ruta+"\\"+nombre+'.csv')
    if(x==2):
        dir=str(input("ingresar la ruta donde se encuentra el archivo a leer: "))    
        leer_csv(dir)
    if(x==3):
        dir=str(input("ingresar la ruta donde se encuentra el archivo a Actualizar: "))
        leer_csv(dir)
        cnt_personas = int(input("ingr/home/labservidores/Documentos/menu\menu.csvar la cantidad de personas a registrar: "))
        llenar(lista, cnt_personas)
        agregar_csv(dir, lista)
        leer_csv(dir)
    if(x==4):
        dir=str(input("ingresar la ruta donde se encuentra el archivo a editar: "))
        cnt_personas = int(input("ingresar el codigo a eliminar: "))
        eliminar_csv(cnt_personas, dir)
        leer_csv(dir)
    if(x==5):
        print((" adios"))