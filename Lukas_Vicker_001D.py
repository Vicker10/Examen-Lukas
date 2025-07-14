productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca:str):
    for i in stock:
        if i in stock:
            if i.lower() == marca.lower():
                return stock[i][1]
   
def stock_marca(marca:str):
    for i in stock:
        if stock[i][0] == marca:
            print("Hay stock!")
        marca_encontrada = stock[i]
        marca_encontrada.insert(0,i)
        return marca_encontrada
    
def busqueda_productos():
    for i in productos:
        print(f"NOMBRE:{productos[i][0]} // MARCA:{productos[i][1]}")

def busqueda_precio(p_minimo:int, p_maximo:int):
    for i in stock:
        if stock[i][1] >= p_minimo and stock[i][1] <= p_maximo:
            print(stock[i])


def actualizar_precio(modelo:str, p:int):
    stock_disponible = stock_marca(modelo)
    if stock_disponible >= p:
        stock[modelo][1] -= p
        print("Precio actualizado!")
        return True
    else:
        print("El modelo no existe!")
        return False
    

def validar_numero_entero_positivo(msg_input:str):
    while True:
        try:
            numero = int(input(msg_input))
            if numero <= 0:
                print("No se puede ingresar numeros negativos o 0!")
                continue
            else:
                return numero
        except ValueError:
            print("Solo se pueden ingresar numeros enteros")
            continue

def validar_texto(mensaje_input):
    while True:
        texto = input(mensaje_input)
        if len(texto.strip()) == 0:
            continue
        else:
            return texto


def menu():
    print("***MENU PRINCIPAL***")
    while True:
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")

        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Solo se permite valores numericos")

        if opcion == 1:
            stock_marca()
        elif opcion == 2:
            p_minimo = validar_numero_entero_positivo("Ingrese el precio minimo: ")
            p_maximo = validar_numero_entero_positivo("Ingrese el precio maximo: ")
            busqueda_precio(p_minimo,p_maximo)
        elif opcion == 3:
            print()

        elif opcion == 4:
            print("Programa finalizado")
            break
        else:
            print("Opcion no valida")    




menu()
