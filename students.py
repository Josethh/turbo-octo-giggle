# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno.
# Definir los métodos para inicializar los atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado ó no.

# Permite crear sistemas más complejos.
# Agiliza el desarrollo de software.
# Facilita el manteniminento del software.
# Fomenta la reutilización y extención del codigo.
# Facilita la creación de programas visuales.
# Relacionar el sistema al mundo real.
# Construcción de prototipos.
# Facilita el trabajo en equipo.

class Student:
    # Método de inicialización de la clase
    def __init__(self):
        # Pide al usuario el nombre del alumno y lo asigna como atributo de la instancia de la clase
        self.name = input('Nombre del alumno: ')
        # Pide al usuario la nota del alumno y la convierte a entero antes de asignarla como atributo de la instancia de la clase
        self.note = int(input('Nota del alumno: ')) 

    # Método para imprimir el nombre y la nota del alumno
    def to_print(self):
        print('Alumno: ', self.name)
        print('Nota: ', self.note)
        print('')

    # Método para imprimir el resultado del alumno (aprobado o reprobado)
    def result(self):
        # Si la nota es menor que 5, el alumno ha reprobado
        if self.note < 5:
            print('El alumno ha reprobado')
        # Si la nota es mayor o igual a 5, el alumno ha aprobado
        else:
            print('El alumno ha aprobado')

        print(' \n ')

# Crea dos instancias de la clase Student
alumno1 = Student()
alumno2 = Student()

# Imprime el nombre y la nota del primer alumno, y su resultado
alumno1.to_print()
alumno1.result()

# Imprime el nombre y la nota del segundo alumno, y su resultado
alumno2.to_print()
alumno2.result()
