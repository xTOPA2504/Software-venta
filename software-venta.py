class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono


class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


# Función para agregar un cliente al archivo clientes.txt
def agregar_cliente():
    # Solicitar los datos del cliente al usuario
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")

    # Escribir los datos del cliente en el archivo de clientes
    with open("clientes.txt", "a") as archivo_clientes:
        archivo_clientes.write(f"{nombre},{direccion},{telefono}\n")

    # Imprimir un mensaje de confirmación en la pantalla
    print("El cliente ha sido agregado correctamente.")


def mostrar_clientes():
    # Leer los datos del archivo de clientes
    with open("clientes.txt", "r") as archivo_clientes:
        datos = archivo_clientes.readlines()

    # Imprimir la lista de clientes en la pantalla
    print("---------------------------------------------------------------------------")
    print("Lista de clientes:")
    for cliente in datos:
        nombre, direccion, telefono = cliente.strip().split(",")
        print(f"Nombre: {nombre} \t\t Dirección: {direccion} \t\t Teléfono: {telefono} \t\t")
        print("---------------------------------------------------------------------------")


def agregar_producto():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = int(input("Ingrese el precio del producto: "))

    # Leer el archivo de productos y almacenar los datos en una variable.
    with open("productos.txt", "r") as f:
        productos = f.readlines()

    # Verificar si el producto ya existe en la lista de productos.
    encontrado = False
    for i, p in enumerate(productos):
        nombre, cantidad_actual, precio_actual = p.strip().split(",")
        if nombre == producto:
            # Sumar la cantidad nueva con la cantidad actual.
            cantidad_nueva = int(cantidad_actual) + cantidad
            productos[i] = f"{nombre},{cantidad_nueva},{precio}\n"
            encontrado = True
            break

    # Si el producto no existe, agregarlo a la lista de productos.
    if not encontrado:
        productos.append(f"{producto},{cantidad},{precio}\n")

    # Escribir los datos actualizados en el archivo de productos.
    with open("productos.txt", "w") as f:
        f.writelines(productos)

    print(f"El producto {producto} se ha agregado correctamente.")


def mostrar_productos():
    # Abrir el archivo de productos en modo "read" (leer)
    with open("productos.txt", "r") as archivo_productos:
        # Leer los datos del archivo y guardarlos en una variable
        datos = archivo_productos.readlines()

    # Imprimir los datos en la pantalla
    print("---------------------------------------------------------------------------")
    print("Lista de productos:")
    for linea in datos:
        descripcion, cantidad, precio = linea.strip().split(",")
        print(f"Descripción: {descripcion} \t\t Cantidad: {cantidad} \t\t Precio: {precio}")
        print("---------------------------------------------------------------------------")


def agregar_venta():
    # Pedimos al usuario que ingrese el cliente
    cliente = input("Ingrese el nombre del cliente: ")

    # Verificamos si el cliente existe en el archivo de clientes
    with open("clientes.txt", "r") as f:
        clientes = f.readlines()
    if not any(cliente in c for c in clientes):
        # Si el cliente no existe, le pedimos su dirección y teléfono y lo agregamos al archivo de clientes
        direccion = input("Ingrese la dirección del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        with open("clientes.txt", "a") as f:
            f.write(f"{cliente},{direccion},{telefono}\n")
        print(f"El cliente {cliente} se agregó correctamente.")

    # Pedimos al usuario que ingrese el nombre del producto
    producto = input("Ingrese el nombre del producto: ")

    # Verificamos si el producto existe en el archivo de productos
    with open("productos.txt", "r") as f:
        productos = f.readlines()
    if not any(producto in p.split(",")[0] for p in productos):
        print("El producto no existe en el archivo de productos.")
        return

    # Obtenemos la cantidad disponible del producto
    cantidad_disponible = int([p.split(",")[1] for p in productos if producto in p.split(",")[0]][0])

    # Si el producto existe, pedimos al usuario que ingrese la cantidad que quiere comprar
    cantidad = input("Ingrese la cantidad que desea comprar: ")
    while not cantidad.isnumeric():
        cantidad = input("Ingrese una cantidad válida: ")
    cantidad = int(cantidad)

    if cantidad_disponible >= cantidad:
        # Si el producto está disponible, lo agregamos a la venta
        precio = int([p.split(",")[2] for p in productos if producto in p.split(",")[0]][0])
        total = cantidad * precio
        with open("ventas.txt", "a") as f:
            f.write(f"{cliente},{producto},{cantidad},{total}\n")

        # Actualizamos el stock del producto
        with open("productos.txt", "w") as f:
            for line in productos:
                if line.startswith(producto):
                    p_nombre, p_cantidad, p_precio = line.strip().split(",")
                    p_cantidad = int(p_cantidad) - cantidad
                    f.write(f"{p_nombre},{p_cantidad},{p_precio}\n")
                else:
                    f.write(line)

        # Calculamos el total por cliente
        with open("ventas.txt", "r") as f:
            ventas = f.readlines()


def mostrar_ventas():
    # Abrimos el archivo de ventas
    with open("ventas.txt", "r") as f:
        ventas = f.readlines()

    # Si no hay ventas, imprimimos un mensaje y terminamos la función
    if not ventas:
        print("No hay ventas registradas.")
        return

    # Imprimimos las ventas
    print("---------------------------------------------------------------------------")
    print("Lista de ventas:")
    for venta in ventas:
        cliente, producto, cantidad, total = venta.strip().split(",")
        print(f"Cliente: {cliente} \t\t Producto: {producto} \t\t Cantidad: {cantidad} \t\t Total: {total}")
        print("---------------------------------------------------------------------------")


# Menú principal
while True:
    print("-------------------------------------------------------------")
    print("1. Gestión de clientes")
    print("2. Gestión de productos")
    print("3. Gestión de ventas")
    print("4. Salir")
    print("-------------------------------------------------------------")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        # Menú de gestión de clientes
        while True:
            print("-------------------------------------------------------------")
            print("1. Agregar cliente")
            print("2. Mostrar clientes")
            print("3. Volver al menú principal")
            print("-------------------------------------------------------------")

            opcion_cliente = input("Ingrese una opción: ")

            if opcion_cliente == "1":
                agregar_cliente()
            elif opcion_cliente == "2":
                mostrar_clientes()
            elif opcion_cliente == "3":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "2":
        # Menú de gestión de productos
        while True:
            print("-------------------------------------------------------------")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Volver al menú principal")
            print("-------------------------------------------------------------")

            opcion_producto = input("Ingrese una opción: ")

            if opcion_producto == "1":
                agregar_producto()
            elif opcion_producto == "2":
                mostrar_productos()
            elif opcion_producto == "3":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "3":
        # Menú de gestión de ventas
        while True:
            print("-------------------------------------------------------------")
            print("1. Agregar venta")
            print("2. Mostrar ventas")
            print("3. Volver al menú principal")
            print("-------------------------------------------------------------")

            opcion_venta = input("Ingrese una opción: ")

            if opcion_venta == "1":
                agregar_venta()
            elif opcion_venta == "2":
                mostrar_ventas()
            elif opcion_venta == "3":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")