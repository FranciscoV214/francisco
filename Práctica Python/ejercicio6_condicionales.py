def condicion_final(nota):
    valoracion= "Aprobado negrito te podes ir a casa tqm"
    if nota <6:
        valoracion= "Deprobado ahre"
    return valoracion


print("Clasificador de notas para estudiantes, Francisco Villarreal 2025 quiero conseguir un laburo ahre")
nota=int(input("Ingrese la nota del estudiante:"))
condicion=condicion_final(nota)
print(condicion)