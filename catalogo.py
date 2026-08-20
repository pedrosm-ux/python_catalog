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

while True:
    print("\n1. Agregar libro")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        break
    else:
        print("Opción inválida.")