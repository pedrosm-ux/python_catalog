catalogo_libros = {
    "El Hobbit": {
        "autor": "Tolkien",
        "anio": 1937,
        "leido": True
    },
    "Harry Potter": {
        "autor": "J.K. Rowling",
        "anio": 1997,
        "leido": True
    }
}

def agregar_libro():
    nombre = input("Ingrese el nombre del libro: ")
    autor = input("Ingrese el autor: ")
    anio = int(input("Ingrese el año: "))
    leido = input("¿Lo ha leído? (si/no): ")

    if leido == "si":
        leido = True
    else:
        leido = False

    catalogo_libros[nombre] = {
        "autor": autor,
        "anio": anio,
        "leido": leido
    }

    print("Libro agregado correctamente.")

def ver_libros():
    for nombre, datos in catalogo_libros.items():
        print("\nLibro:", nombre)
        print("Autor:", datos["autor"])
        print("Año:", datos["anio"])
        print("Leído:", datos["leido"])

def modificar_libro():
    nombre = input("Ingrese el nombre del libro que desea modificar: ")

    if nombre in catalogo_libros:
        atributo = input("¿Qué desea modificar? (autor/anio/leido): ")

        if atributo == "autor":
            nuevo_autor = input("Ingrese el nuevo autor: ")
            catalogo_libros[nombre]["autor"] = nuevo_autor

        elif atributo == "anio":
            nuevo_anio = int(input("Ingrese el nuevo año: "))
            catalogo_libros[nombre]["anio"] = nuevo_anio

        elif atributo == "leido":
            nuevo_leido = input("¿Lo ha leído? (si/no): ")

            if nuevo_leido == "si":
                catalogo_libros[nombre]["leido"] = True
            else:
                catalogo_libros[nombre]["leido"] = False

        else:
            print("Atributo inválido.")

        print("Libro modificado correctamente.")

    else:
        print("El libro no existe.")

while True:
    print("\n1. Ver todos los libros")
    print("2. Agregar libro")
    print("3. Modificar un libro")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ver_libros()
    elif opcion == "2":
        agregar_libro()
    elif opcion == "3":
        modificar_libro()
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")