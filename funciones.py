import os,time
detalle_pedidos = []
cinco_kl = 12500
quince_kl = 25500
def menu():
    while True:
        os.system('cls')
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos")
        print("3. Buscar pedido por RUT")
        print("4. Imprimir hoja de ruta")
        print("5. Salir")
        opc = input("Ingrese opción: ")
        if opc == "1":
            registrar_pedido()
        elif opc == "2":
            listar_pedido()
        elif opc == "3":
            buscar_pedido()
        elif opc == "4":
            imprimir_hoja()
        else:
            salir()

def registrar_pedido():
    print("REGISTRAR PEDIDO")
    rut = int(input("Ingrese rut sin digito verificador: "))
    nombre = input("Ingrese su nombre: ")
    direccion = input ("Ingrese su direccion: ")
    comuna = input("Ingrese su comuna(Santiago, Colina, Pirque): ")
    cilindro_5 = int(input("Ingrese cantidad de cilindros de 5 kg: "))
    cilindro_15 = int(input("Ingrese cantidad de cilindros de 15 kg: "))
    total = (cilindro_5*cinco_kl)+(cilindro_15*quince_kl)
    detalle_pedido = {"RUT":rut,
                      "NOMBRE":nombre,
                      "DIRECCION":direccion,
                      "COMUNA":comuna,
                      "5KG":cilindro_5,
                      "15KG":cilindro_15,
                      "TOTAL":total}
    detalle_pedidos.append(detalle_pedido)

def listar_pedido():
    print("LISTAR PEDIDO")
    for p in detalle_pedidos:
        print(f"RUT:{p['RUT']},NOMBRE:{p['NOMBRE']},DIRECCION:{p['DIRECCION']},COMUNA:{p['COMUNA']},5KG:{p['5KG']},15KG:{p['15KG']},TOTAL{p['TOTAL']}")
def buscar_pedido():
    if not detalle_pedidos:
        print("NO SE ENCUENTRAN PEDIDOS ACTUALMENTE PORFAVOR HAGA UNO ")
    else:
        busc_pedido = int(input("Ingrese rut sin digito verificador: "))
        if busc_pedido in detalle_pedidos:
            print("TU PEDIDO ES",detalle_pedidos)
        else:
            print("NO SE ENCONTRO PEDIDO")
            return

def imprimir_hoja():
    if not detalle_pedidos:
        print("NO HAY PEDIDOS PARA IMPRIMIR")
    else:
            try:
                import csv
                archivo = input("Ingrese nombre del archivo: ")+".csv"
                sectores = input("Ingrese sector(Santiago,Colina.Pirque): ") 
                with open(archivo,'x',newline="")as archivo:
                    sectores(f"RUT:{['RUT']},NOMBRE:{['NOMBRE']},DIRECCION:{['DIRECCION']},COMUNA:{['COMUNA']},5KG:{['5KG']},15KG:{['15KG']},TOTAL{['TOTAL']}")
                    
            except:
                print("EL ARCHIVO YA EXISTE")

def validar_nombre():
    nom = input("Ingrese su nombre: ")
    if len(nom)>=3:
        print("nombre agregado")
    else:
        print("ERROR EL NOMBRE DEBE TENER MAS DE 3 LETRAS")
        return nom

def salir():
    print("ADIOS VUELVA PRONTO")
    return

