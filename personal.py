print("")
print("***************************")
print("**      BIENVENIDO A     **")
print("*** LA TIENDITA DE MAYA ***")
print("***************************")

productos = {"Camisa": {"Precio": 10, "Cantidad": 25 },
             "Pantalon": {"Precio": 15, "Cantidad": 20},
             "Zapatos": {"Precio": 25, "Cantidad": 20},
             "Falda": {"Precio": 10, "Cantidad": 16},
             "Shorts": {"Precio": 12, "Cantidad": 24},
             "Sandalias": {"Precio": 20, "Cantidad": 14}}

carrito = {}

def inventario(productos):
    print('')
    print('Actualmente, en la tiendita tenemos disponible:')
    print('')
    print('*******************************************************************')
    print('Producto               Precio                 Cantidad Disponible')
    print('*******************************************************************')
    for llave, valor in productos.items():
        print(f"{llave:<10}               {valor["Precio"]:<10}                   {valor["Cantidad"]:<10}")
    print('*******************************************************************')
    print('')
    print('')

def comprar(productos,carrito):
    while True:
        print('')
        print('************************************************')
        print('Por favor, indica el producto que deseas comprar:')
        print('************************************************')
        producto=input()
        if producto not in productos:
            print('')
            print('*****************************************')
            print('Lo sentimos, no contamos con ese producto')
            print('*****************************************')
            print('')
        else:
            print('***********************************************************')
            print(f'Ahora, indica la cantidad de {producto} que deseas comprar:')
            print('***********************************************************')
            cant = int(input())
            
            if productos[producto]["Cantidad"] < cant:
                print('')
                print('*****************************************')
                print('Lo sentimos, no contamos con esa cantidad')
                print('*****************************************')
                print('')
            else:
                productos[producto]["Cantidad"] -= cant
                carrito[producto]={"Precio": productos[producto]["Precio"], "Cantidad": cant}
                print('*****************************************')
                print("¿Deseas agregar mas productos al carrito?")
                print('         (S para SI y N para NO)         ')
                print('*****************************************')
                opc=input()
                #if opc=='S' or opc=='s':
                    #comprar(productos, carrito)
                if opc=='N' or opc=='n':
                    print('')
                    print('******************************')
                    print('Compra realizada exitosamente!')
                    print('******************************')
                    print('')
                    break

def ver_carrito(carrito):
    print('')
    total=0
    print('********************************************************************************************')
    print('Producto           Precio Unitario            Cantidad Comprada                    Total')
    print('********************************************************************************************')
    for llave,valor in carrito.items():
        precio= valor["Precio"]*valor["Cantidad"]
        print(f"{llave:<10}               {valor["Precio"]:<10}                   {valor["Cantidad"]:<10}                     {precio:<10}")
        total += precio
    print('********************************************************************************************')
    print('')
    print('*********************')
    print(f'Total pagado: {total}')
    print('*********************')
    print('')
    print('')

def menu():
    print('*****************************')
    print('1.- Ver productos disponibles')
    print('2.- Comprar productos')
    print('3.- Ver tu carrito de compras')
    print('4.- Salir del programa')
    print('*****************************')

print('Por favor, ingresa tu nombre: ')
nombre=input()
print('')
print('********************************************************************')
print(f'Hola, {nombre}! Por favor indica la opcion que deseas llevar a cabo:')
print('********************************************************************')
print('')
while True:
    menu()
    opc=int(input())
    if opc==1:
        inventario(productos)
    elif opc==2:
        comprar(productos,carrito)
    elif opc==3:
        ver_carrito(carrito)
    elif opc==4:
        print('************************')
        print('Gracias por tu visita! :)')
        print('************************')
        print('Saliendo del programa...')
        break
    else:
        print('')
        print('************************************')
        print('Por favor, ingresa una opcion valida')
        print('************************************')
        print('')
