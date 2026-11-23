class PlaylistFestival:
    def __init__(self):
        self.nombres = []
        self.artistas = []
        self.duraciones = []
        self.popularidades = []

    def agregar_canciones(self):
        cantidad = int(input("Cuantas canciones quieres agregar? "))
        while cantidad <= 0:
            print("Escribe un numero mayor a 0")
            cantidad = int(input("Cuantas canciones quieres agregar? "))

        for i in range(cantidad):
            print("Cancion", i + 1)
            nombre = input("Nombre: ")
            artista = input("Artista: ")

            while True:
                duracion = float(input("Duracion en minutos: "))
                if duracion > 0:
                    break
                print("La duracion debe ser mayor a 0")

            while True:
                popularidad = int(input("Popularidad (1-100): "))
                if 1 <= popularidad <= 100:
                    break
                print("Debe estar entre 1 y 100")

            self.nombres.append(nombre)
            self.artistas.append(artista)
            self.duraciones.append(duracion)
            self.popularidades.append(popularidad)

    def ver_reportes(self):
        if len(self.nombres) == 0:
            print("No hay canciones registradas")
            return

        total = len(self.nombres)
        duracion_total = sum(self.duraciones)
        promedio_pop = sum(self.popularidades) / total

        idx_mas_pop = 0
        idx_menos_pop = 0

        for i in range(total):
            if self.popularidades[i] > self.popularidades[idx_mas_pop]:
                idx_mas_pop = i
            if self.popularidades[i] < self.popularidades[idx_menos_pop]:
                idx_menos_pop = i

        print("\nReportes")
        print("Total de canciones:", total)
        print("Duracion total (min):", round(duracion_total, 2))
        print("Cancion mas popular:", self.nombres[idx_mas_pop], "-", self.artistas[idx_mas_pop], "(Popularidad:", self.popularidades[idx_mas_pop], ")")
        print("Cancion menos popular:", self.nombres[idx_menos_pop], "-", self.artistas[idx_menos_pop], "(Popularidad:", self.popularidades[idx_menos_pop], ")")
        print("Promedio de popularidad:", round(promedio_pop, 2))

    def buscar_canciones(self):
        if len(self.nombres) == 0:
            print("No hay canciones registradas")
            return

        print("1. Buscar por artista")
        print("2. Buscar por rango de popularidad")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            artista_buscado = input("Artista a buscar: ").lower()
            encontradas = 0
            for i in range(len(self.nombres)):
                if self.artistas[i].lower() == artista_buscado:
                    print(self.nombres[i], "-", self.artistas[i], "| Duracion:", self.duraciones[i], "| Popularidad:", self.popularidades[i])
                    encontradas += 1
            if encontradas == 0:
                print("No se encontraron canciones de ese artista")

        elif opcion == "2":
            min_pop = int(input("Popularidad minima (1-100): "))
            max_pop = int(input("Popularidad maxima (1-100): "))
            encontradas = 0
            for i in range(len(self.nombres)):
                if min_pop <= self.popularidades[i] <= max_pop:
                    print(self.nombres[i], "-", self.artistas[i], "| Duracion:", self.duraciones[i], "| Popularidad:", self.popularidades[i])
                    encontradas += 1
            if encontradas == 0:
                print("No se encontraron canciones en ese rango")

        else:
            print("Opcion no valida")

    def playlist_recomendada(self):
        if len(self.nombres) == 0:
            print("No hay canciones registradas")
            return

        promedio_pop = sum(self.popularidades) / len(self.nombres)
        print("\nPlaylist recomendada (popularidad mayor a", round(promedio_pop, 2), ")")

        encontradas = 0
        for i in range(len(self.nombres)):
            if self.popularidades[i] > promedio_pop:
                print(self.nombres[i], "-", self.artistas[i], "| Duracion:", self.duraciones[i], "| Popularidad:", self.popularidades[i])
                encontradas += 1

        if encontradas == 0:
            print("Ninguna cancion supera el promedio")


playlist = PlaylistFestival()

while True:
    print("\n1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        playlist.agregar_canciones()
    elif opcion == "2":
        playlist.ver_reportes()
    elif opcion == "3":
        playlist.buscar_canciones()
    elif opcion == "4":
        playlist.playlist_recomendada()
    elif opcion == "5":
        print("Saliendo del programa")
        break
    else:
        print("Opcion no valida")