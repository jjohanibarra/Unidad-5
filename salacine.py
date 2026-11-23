class SalaCine:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append("L")
            self.matriz.append(fila)

    def mostrar_sala(self):
        print("\nSala de cine")
        for fila in self.matriz:
            print(" ".join(fila))

    def asiento_valido(self, fila, columna):
        return 1 <= fila <= self.filas and 1 <= columna <= self.columnas

    def reservar_asiento(self, fila, columna):
        if not self.asiento_valido(fila, columna):
            print("Ese asiento no existe")
            return
        if self.matriz[fila - 1][columna - 1] == "X":
            print("Ese asiento ya esta ocupado")
        else:
            self.matriz[fila - 1][columna - 1] = "X"
            print("Asiento reservado")

    def liberar_asiento(self, fila, columna):
        if not self.asiento_valido(fila, columna):
            print("Ese asiento no existe")
            return
        if self.matriz[fila - 1][columna - 1] == "L":
            print("Ese asiento ya esta libre")
        else:
            self.matriz[fila - 1][columna - 1] = "L"
            print("Asiento liberado")

    def contar_asientos(self):
        libres = 0
        ocupados = 0
        for fila in self.matriz:
            for asiento in fila:
                if asiento == "L":
                    libres += 1
                else:
                    ocupados += 1
        return libres, ocupados


filas = int(input("Numero de filas: "))
columnas = int(input("Numero de columnas: "))

while filas <= 0 or columnas <= 0:
    print("Escribe numeros mayores a 0")
    filas = int(input("Numero de filas: "))
    columnas = int(input("Numero de columnas: "))

sala = SalaCine(filas, columnas)

while True:
    print("\n1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        sala.mostrar_sala()
    elif opcion == "2":
        f = int(input("Fila: "))
        c = int(input("Columna: "))
        sala.reservar_asiento(f, c)
    elif opcion == "3":
        f = int(input("Fila: "))
        c = int(input("Columna: "))
        sala.liberar_asiento(f, c)
    elif opcion == "4":
        libres, ocupados = sala.contar_asientos()
        print("Asientos libres:", libres)
        print("Asientos ocupados:", ocupados)
    elif opcion == "5":
        print("Saliendo del programa")
        break
    else:
        print("Opcion no valida")