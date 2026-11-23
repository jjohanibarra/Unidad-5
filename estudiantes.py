class Grupo:
    def __init__(self, estudiantes, materias):
        self.estudiantes = estudiantes
        self.materias = materias
        self.matriz = []

    def capturar(self):
        for i in range(self.estudiantes):
            fila = []
            print("Estudiante", i + 1)
            for j in range(self.materias):
                while True:
                    nota = float(input("Calificacion materia " + str(j + 1) + " (0-100): "))
                    if 0 <= nota <= 100:
                        fila.append(nota)
                        break
                    print("Debe ser entre 0 y 100")
            self.matriz.append(fila)

    def promedios_estudiantes(self):
        promedios = []
        for fila in self.matriz:
            promedios.append(sum(fila) / self.materias)
        return promedios

    def promedios_materias(self):
        promedios = []
        for j in range(self.materias):
            suma = 0
            for i in range(self.estudiantes):
                suma += self.matriz[i][j]
            promedios.append(suma / self.estudiantes)
        return promedios

    def mayor_calificacion(self):
        mayor = self.matriz[0][0]
        for fila in self.matriz:
            for nota in fila:
                if nota > mayor:
                    mayor = nota
        return mayor

    def menor_calificacion(self):
        menor = self.matriz[0][0]
        for fila in self.matriz:
            for nota in fila:
                if nota < menor:
                    menor = nota
        return menor

    def contar_aprobados_reprobados(self, minima=70):
        promedios = self.promedios_estudiantes()
        aprobados = 0
        reprobados = 0
        for prom in promedios:
            if prom >= minima:
                aprobados += 1
            else:
                reprobados += 1
        return aprobados, reprobados


estudiantes = int(input("Cuantos estudiantes son? "))
materias = int(input("Cuantas materias son? "))

while estudiantes <= 0 or materias <= 0:
    print("Escribe numeros mayores a 0")
    estudiantes = int(input("Cuantos estudiantes son? "))
    materias = int(input("Cuantas materias son? "))

grupo = Grupo(estudiantes, materias)
grupo.capturar()

prom_est = grupo.promedios_estudiantes()
prom_mat = grupo.promedios_materias()
aprobados, reprobados = grupo.contar_aprobados_reprobados()

print("\nResultados")
for i in range(estudiantes):
    print("Estudiante", i + 1, ":", grupo.matriz[i], "Promedio:", round(prom_est[i], 2))

print("\nPromedio por materia")
for j in range(materias):
    print("Materia", j + 1, ":", round(prom_mat[j], 2))

print("\nCalificacion mas alta:", grupo.mayor_calificacion())
print("Calificacion mas baja:", grupo.menor_calificacion())
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)