juegos =["MINECRAFT", "GTAV", "RED2"]

print("===iINVETARIO DE VIDEOJUEGOS ")
print("1. ver mis juegos ")
print("2. agregar juego nuevo ")
print("3. borrar juego")
print("4. salir")


while True:
    opcion = input("\nElige una opcion 1-4:")
    
    if opcion == "1":
        print("\nTus juegos:")
        if len(juegos) == 0:
            print("aun no tienes juegos")
        else:
            for i, juego in enumerate(juegos, 1):
                print(f"{i}. {juego}")
        
                
    elif opcion == "2":
        nuevo = input("nombre del juego nuevo:")
        juegos.append(nuevo)
        print(f"{nuevo} agregado al inventario")
        
    elif opcion == "3":
        if len(juegos) == 0:
            print(" no ay juegos que borrar")
        else:
            borrar = input("nombre del juego exacto a borrar:")
            if borrar in juegos:
                juegos.remove(borrar)
                print(f"{borrar} eliminado")
            else:
                print("ese juego ya no esta en tu invetario")
                
                
    elif opcion == "4":
        print("guardando invetario... Adios")
        break
    
    else:
        print("opcion no valida. usa 1, 2, 3, o 4")                                                   