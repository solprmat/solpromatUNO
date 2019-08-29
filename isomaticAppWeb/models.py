from django.db import models

# Create your models here.


# Todo primeros paso py manager.py makemigrations
# Todo segundo comando py manager.py migrate
# TODO CREAR OBJETO ESTUDIANTE  SIEMPRE HACER py manager.py migrate
class Estudiante(models.Model):
    nombreCompleto  = models.CharField(max_length=40, help_text="Ingrese Su nombre Completo", blank=False , null=False)
    sexo = models.CharField(max_length=1, help_text="ingrese su Sexo Ejemplo M = Masculino, F = Femenino", blank=False , null=False)
    curso = models.CharField(max_length=10, help_text= "801 - 802 - 803 - 804", blank=False , null=False)
    estrato = models.IntegerField( help_text="1 - 2 - 3 - 4", blank=False , null=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    registrado = models.BooleanField(default=False)


    def __str__(self):
        template = '{0.id}, {0.nombreCompleto}, {0.sexo}, {0.curso}, {0.estrato},{0.registrado}, {0.fecha_registro},{0.registrado}'
        return template.format(self)
        # return self.nombreCompleto

class Pregunta1(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta1',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P01 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaUno = models.CharField(max_length=255, blank=False , null=False)
    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P01}, {0.preguntaGuardada},{0.respuestaCorrectaUno}'
        return template.format(self)

# pregunta 2 de imagenes
class Pregunta2(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta2',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P02 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaDos = models.CharField(max_length=255, blank=False, null=False)
    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P02}, {0.preguntaGuardada},{0.respuestaCorrectaDos}'
        return template.format(self)
# pregunta 3

class Pregunta3(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta3',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P03 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaTres = models.CharField(max_length=255, blank=False, null=False)

    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P03}, {0.preguntaGuardada},{0.respuestaCorrectaTres}'
        return template.format(self)

# pregunta 4
class Pregunta4(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta4',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P04 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaCuatro = models.CharField(max_length=255, blank=False, null=False)

    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P04}, {0.preguntaGuardada},{0.respuestaCorrectaCuatro}'
        return template.format(self)

# pregunta 5
class Pregunta5(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta5',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P05 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaCinco = models.CharField(max_length=255, blank=False, null=False)

    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P05}, {0.preguntaGuardada},{0.respuestaCorrectaCinco}'
        return template.format(self)

# pregunta 6
class Pregunta6(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta6',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P06 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaSeis = models.CharField(max_length=255, blank=False, null=False)

    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P06}, {0.preguntaGuardada},{0.respuestaCorrectaSeis}'
        return template.format(self)


# pregunta 7
class Pregunta7(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta7',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P07 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaSiete = models.CharField(max_length=255, blank=False, null=False)

    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P07}, {0.preguntaGuardada},{0.respuestaCorrectaSiete}'
        return template.format(self)

# pregunta 8
class Pregunta8(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta8',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P08 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaOcho = models.CharField(max_length=255, blank=False, null=False)

    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P08}, {0.preguntaGuardada},{0.respuestaCorrectaOcho}'
        return template.format(self)

# pregunta 9
class Pregunta9(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta9',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P09 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaNueve = models.CharField(max_length=255, blank=False, null=False)

    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P09}, {0.preguntaGuardada},{0.respuestaCorrectaNueve}'
        return template.format(self)

# pregunta 10
class Pregunta10(models.Model):
    # Todo si el atributo on_delete se pone en CASCADE por todo lo del hijo y del padre
    identificadorEstudiante = models.ForeignKey(Estudiante, related_name='Pregunta10',on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255, blank=False , null=False)
    fecha_registro_P010 = models.DateTimeField(auto_now_add=True)
    preguntaGuardada = models.BooleanField(default=False)
    respuestaCorrectaDiez = models.CharField(max_length=255, blank=False, null=False)

    # TODO falta implementar el cronometro tiempo que se demora el estudiante

    def __str__(self):
        template = '{0.identificadorEstudiante}, {0.respuesta}, {0.fecha_registro_P010}, {0.preguntaGuardada},{0.respuestaCorrectaDiez}'
        return template.format(self)

# class RespuestasEstudiante(models.Model):
