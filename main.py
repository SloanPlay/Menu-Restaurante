menu = [
    "Hamburguesa",
    "Pizza",
    "Hot Dog",
    "Tacos",
    "Pollo Frito",
    "Ensalada",
    "Sándwich",
    "Empanada",
    "Batida",
    "Refresco"
]

precios = [250, 400, 150, 200, 300, 180, 220, 100, 160, 80]

ventas = []


def mostrar_menu():
    print("\n=== MENÚ DEL RESTAURANTE ===")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")
    print("0. Finalizar y ver factura")


def capturar_venta():
    while True:
        mostrar_menu()
        opcion = input("Seleccione un producto (0 para terminar): ")
        
        if opcion == "0":
            break
        
        if opcion.isdigit() and 1 <= int(opcion) <= 10:
            ventas.append(int(opcion) - 1)
            print("Venta registrada.\n")
        else:
            print("Opción inválida. Intente nuevamente.\n")


def mostrar_factura():
    print("\n============================")
    print("         FACTURA")
    print("============================")

    total_general = 0

    for i in range(10):
        cantidad = ventas.count(i)
        
        if cantidad > 0:   
            total = cantidad * precios[i]
            total_general += total

            print(f"{menu[i]}  x{cantidad}  -  {total} pesos")

    print("----------------------------")
    print(f"TOTAL A PAGAR: {total_general} pesos")
    print("============================\n")



capturar_venta()
mostrar_factura()
