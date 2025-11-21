menu = [
    "1. Hamburguesa",
    "2. Pizza",
    "3. Hot Dog",
    "4. Tacos",
    "5. Pollo Frito",
    "6. Ensalada",
    "7. Sándwich",
    "8. Empanada",
    "9. Batida",
    "10. Refresco"
]

precios = [250, 400, 150, 200, 300, 180, 220, 100, 160, 80]


ventas = []


def mostrar_menu():
    print("\n=== MENÚ DEL RESTAURANTE ===")
    for item in menu:
        print(item)
    print("0. Finalizar y ver reporte")


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


def mostrar_reporte():
    print("\n=== REPORTE DE VENTAS ===")
    
    total_general = 0
    
    for i in range(10):
        cantidad = ventas.count(i)
        total = cantidad * precios[i]
        total_general += total
        
        print(f"{menu[i]} - Vendidos: {cantidad} - Total: {total} pesos")
    
    print(f"\nTOTAL GENERAL DE VENTAS: {total_general} pesos")


capturar_venta()
mostrar_reporte()
