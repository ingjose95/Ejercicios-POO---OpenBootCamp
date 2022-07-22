class Alumno:

    def informacionAlumno(self, nombre, nota):

        self.nombre = nombre
        self.nota = nota


    def datosAlumno(self):

        print('El nombre del alumno es: ', self.nombre, '\nLa nota del alumno es: ', self.nota, ' puntos')

    def resultadoAlumno(self):

        if self.nota >= 10:

            print('El alumno ha aprobado. ¡Felicitaciones!')

        else:

            print('El alumno no ha aprobado. Sigue esforzándote.')

# se crea el alumno y se muestran sus datos por pantalla
a = Alumno()
a.informacionAlumno('José', 18)
a.datosAlumno()

# se evalua si el alumno aprobó o no

a.resultadoAlumno()

# se crea un segundo alumno y se muestran sus datos por pantalla
a2 = Alumno()
a2.informacionAlumno('Juan', 7)
a2.datosAlumno()

# se evalua si el alumno aprobó o no

a2.resultadoAlumno()
