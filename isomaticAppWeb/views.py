# TODO PARA EL CORREO
from django.conf import settings
from django.core.mail import send_mail
from django.core.cache import cache

from django.shortcuts import render, redirect
from django.contrib import messages
# importar formulario
from psycopg2._psycopg import DataError
from django.http import HttpResponseRedirect

from .formulario import RegistrarEstudiante
from .preguntaUno import PreguntaUno
from .preguntaDos import PreguntaDos
from .preguntaTres import PreguntaTres
from .preguntaCuatro import PreguntaCuatro
from .preguntaCinco import PreguntaCinco
from .preguntaSeis import PreguntaSeis
from .preguntaSiete import PreguntaSiete
from .preguntaOcho import PreguntaOcho
from .preguntaNueve import PreguntaNueve
from .preguntaDiez import PreguntanDiez

# Create your views here.

from .models import *

# TODO variable global para guardar la llave foranea del estudiante y utilizarla en las 10 preguntas


pk = 0


# Todo Primer inndex
def inicio(request):
    # //ip = request.body.find()
    # //print('Pruebas POST '+ str(ip))
    print('******************************* RETORNANDO EL REQUEST' + request.path)
    return render(request, "index.html", {})


def formularioUsuario(request):
    try:

        # titulo = "Hola"
        # # Todo para saber el usuario que esta autenticado
        # if request.user.is_authenticated:
        #     titulo = "Bienvenido %s" %(request.user)
        formulario = RegistrarEstudiante(request.POST or None)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            # Tomar los datos de presentacion
            nombreCompleto = datos.get("nombreCompleto")
            sexo = datos.get("sexo")
            curso = datos.get("curso")
            estrato = datos.get("estrato")
            fecha_registro = datos.get("fecha_registro")
            registrado = True
            # print('''************************ nombre''' + nombreCompleto)

            # guardar objeto
            objeto = Estudiante.objects.create(nombreCompleto=nombreCompleto,
                                               sexo=sexo,
                                               curso=curso, estrato=estrato,
                                               fecha_registro=fecha_registro, registrado=registrado)
            objeto.save()
            pk = objeto.pk
            # print('********************* llave foranea  ', pk)
            asunto = 'Registro de estudiante Exitoso Plataforma SOLPROMAT'
            email_from = settings.EMAIL_HOST_USER
            # aqui se pueden poner otros correos
            # , "aleja1987@gmail.com"
            email_to = [email_from,"aleja1987@gmail.com"]
            email_mensaje = "Mensaje de Aviso con el Registro Exitosamente del Usuario %s" % (nombreCompleto)
            send_mail(
                asunto,
                email_mensaje,
                email_from,
                email_to,
                fail_silently=False
            )
            # print('Se envio el Correo')
            # print('SE GUARDO EL OBJETO ESTUDIANTE')
            messages.success(request, 'Estudiante ' + nombreCompleto + ' se  Registro Exitosamente')

            # print('************el objeto del estudiante se guardo con exito *******************')
            response = redirect('/preguntaUno/' + str(pk))
            print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
            # return render(request, 'preguntaUno.html',{})

        context = {
            "el_formulario": formulario,
        }
        # print('******************************* RETORNANDO EL REQUEST 2' + request.path)
        return render(request, "formularioUsuario.html", context)
    except ValueError as e:
        print("Error al Registrar el Estudiante: {0}".format(e))
        # messages.error(request, 'Error al Registrar el Estudiante',e.pgerror)


# ***********************************************************************
def preguntaUno(request, pk):
    respuestaUno = 'c'
    try:
        # print('*********** llave de primaria ' + str(identificadorEstudiante))
        formularioPreguntaUno = PreguntaUno(request.POST or None)

        if formularioPreguntaUno.is_valid():
            datosUno = formularioPreguntaUno.cleaned_data
            respuesta = datosUno.get("respuesta")
            fecha_registro_P01 = datosUno.get("fecha_registro_P01")
            preguntaGuardada = True
            # Todo pasar la llave que tenemos del usuario
            # idEstudiante_global =  globals()['idEstudiante_global']
            # print('********************* llave foranea  ', idEstudiante_global)
            identificadorEstudianteUno = Estudiante.objects.get(id=pk)
            print('objecto ', identificadorEstudianteUno)
            objetoPregunta1 = Pregunta1.objects.create(respuesta=respuesta, fecha_registro_P01=fecha_registro_P01,
                                                       preguntaGuardada=preguntaGuardada,
                                                       identificadorEstudiante=identificadorEstudianteUno,
                                                       respuestaCorrectaUno=respuestaUno)
            objetoPregunta1.save()
            # print('************el objeto del Pregunta 1 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 1 Exitosamente')
            # return render(request, "pregunta2.html", {})
            response = redirect('/pregunta2/' + str(pk))
            print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formularioPreguntaUno": formularioPreguntaUno,
        }

        return render(request, "preguntaUno.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 1: {0}".format(e.with_traceback()))


# *******************************************************************
def preguntaDos(request, pk):
    respuestaDos = 'a'

    try:
        formularioPreguntaDos = PreguntaDos(request.POST or None)
        if formularioPreguntaDos.is_valid():
            datosDos = formularioPreguntaDos.cleaned_data
            respuesta = datosDos.get("respuesta")
            fecha_registro_P02 = datosDos.get("fecha_registro_P02")
            preguntaGuardada = True
            # Todo pasar la llave que tenemos del usuario

            # idEstudiante_global = globals()['idEstudiante_global']
            # print('********************* llave foranea pregunta dos ', idEstudiante_global)
            identificadorEstudianteDos = Estudiante.objects.get(id=pk)
            print('objecto ', identificadorEstudianteDos)
            objetoPregunta2 = Pregunta2.objects.create(respuesta=respuesta, fecha_registro_P02=fecha_registro_P02,
                                                       preguntaGuardada=preguntaGuardada,
                                                       identificadorEstudiante=identificadorEstudianteDos,
                                                       respuestaCorrectaDos=respuestaDos)
            objetoPregunta2.save()
            # print('************el objeto del Pregunta 2 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 2 Exitosamente')
            # return render(request, 'pregunta3.html', {})
            response = redirect('/pregunta3/' + str(pk))
            # print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formulario_PreguntaDos": formularioPreguntaDos,
        }
        # / return redirect('pregunta3.html')
        return render(request, "pregunta2.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 3: {0}".format(e.with_traceback()))


# *******************************************************************
def preguntaTres(request, pk):
    respuestaTres = 'b'
    try:
        formularioPreguntaTres = PreguntaTres(request.POST or None)
        if formularioPreguntaTres.is_valid():
            datosTres = formularioPreguntaTres.cleaned_data

            respuesta = datosTres.get("respuesta")
            fecha_registro_P03 = datosTres.get("fecha_registro_P03")
            preguntaGuardada = True
            # idEstudiante_global = globals()['idEstudiante_global']
            # print('*************** llave en la pregunta 3 ', idEstudiante_global)
            identificadorEstudianteTres = Estudiante.objects.get(id=pk)
            objetoPregunta3 = Pregunta3.objects.create(respuesta=respuesta, fecha_registro_P03=fecha_registro_P03,
                                                       preguntaGuardada=preguntaGuardada,
                                                       identificadorEstudiante=identificadorEstudianteTres,
                                                       respuestaCorrectaTres=respuestaTres)
            objetoPregunta3.save()
            # print('************el objeto del Pregunta 3 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 3 Exitosamente')
            # return render(request, "pregunta4.html", {})
            response = redirect('/pregunta4/' + str(pk))
            # print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formulario_PreguntaTres": formularioPreguntaTres,
        }

        return render(request, "pregunta3.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 2: {0}".format(e.with_traceback()))


# ********************* Pregunta 4
def preguntaCuatro(request, pk):
    respuestaCuatro = 'c'
    try:
        formularioPreguntaCuatro = PreguntaCuatro(request.POST or None)
        if formularioPreguntaCuatro.is_valid():
            datosCuatro = formularioPreguntaCuatro.cleaned_data

            respuesta = datosCuatro.get("respuesta")
            fecha_registro_P04 = datosCuatro.get("fecha_registro_P04")
            preguntaGuardada = True
            # Todo pasar la llave que tenemos del usuario
            # idEstudiante_global = globals()['idEstudiante_global']
            # print('*************** llave en la pregunta 3 ', idEstudiante_global)
            identificadorEstudianteCuatro = Estudiante.objects.get(id=pk)
            objetoPregunta4 = Pregunta4.objects.create(respuesta=respuesta, fecha_registro_P04=fecha_registro_P04,
                                                       preguntaGuardada=preguntaGuardada,
                                                       identificadorEstudiante=identificadorEstudianteCuatro,
                                                       respuestaCorrectaCuatro=respuestaCuatro)
            objetoPregunta4.save()
            # print('************el objeto del Pregunta 4 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 4 Exitosamente')
            # return render(request, "pregunta5.html", {})
            response = redirect('/pregunta5/' + str(pk))
            print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formulario_PreguntaCuatro": formularioPreguntaCuatro,
        }

        return render(request, "pregunta4.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 4: {0}".format(e.with_traceback()))


# ********************* Pregunta 5
def preguntaCinco(request, pk):
    respuestaCinco = 'b'
    try:
        formularioPreguntaCinco = PreguntaCinco(request.POST or None)
        if formularioPreguntaCinco.is_valid():
            datosCinco = formularioPreguntaCinco.cleaned_data

            respuesta = datosCinco.get("respuesta")
            fecha_registro_P05 = datosCinco.get("fecha_registro_P05")
            preguntaGuardada = True
            # Todo pasar la llave que tenemos del usuario
            # idEstudiante_global = globals()['idEstudiante_global']
            # print('*************** llave en la pregunta 3 ', idEstudiante_global)
            identificadorEstudianteCinco = Estudiante.objects.get(id=pk)
            objetoPregunta5 = Pregunta5.objects.create(respuesta=respuesta, fecha_registro_P05=fecha_registro_P05,
                                                       preguntaGuardada=preguntaGuardada,
                                                       identificadorEstudiante=identificadorEstudianteCinco,
                                                       respuestaCorrectaCinco=respuestaCinco)
            objetoPregunta5.save()
            # print('************el objeto del Pregunta 5 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 5 Exitosamente')
            # return render(request, "pregunta6.html", {})
            response = redirect('/pregunta6/' + str(pk))
            print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formulario_PreguntaCinco": formularioPreguntaCinco,
        }

        return render(request, "pregunta5.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 5: {0}".format(e.with_traceback()))


# ********************* Pregunta 6
def preguntaSeis(request, pk):
    respuestaSeis = 'a'
    try:
        formularioPreguntaSeis = PreguntaSeis(request.POST or None)
        if formularioPreguntaSeis.is_valid():
            datosSeis = formularioPreguntaSeis.cleaned_data

            respuesta = datosSeis.get("respuesta")
            fecha_registro_P06 = datosSeis.get("fecha_registro_P06")
            preguntaGuardada = True
            # Todo pasar la llave que tenemos del usuario
            # idEstudiante_global = globals()['idEstudiante_global']
            # print('*************** llave en la pregunta 6 ', idEstudiante_global)
            identificadorEstudianteSeis = Estudiante.objects.get(id=pk)
            objetoPregunta6 = Pregunta6.objects.create(respuesta=respuesta, fecha_registro_P06=fecha_registro_P06,
                                                       preguntaGuardada=preguntaGuardada,
                                                       identificadorEstudiante=identificadorEstudianteSeis,
                                                       respuestaCorrectaSeis=respuestaSeis)
            objetoPregunta6.save()
            # print('************el objeto del Pregunta 6 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 6 Exitosamente')
            # return render(request, "pregunta7.html", {})
            response = redirect('/pregunta7/' + str(pk))
            # print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formulario_PreguntaSeis": formularioPreguntaSeis,
        }

        return render(request, "pregunta6.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 6: {0}".format(e.with_traceback()))


# ********************* Pregunta 7
def preguntaSiete(request, pk):
    respuestaSiete = 'd'
    try:
        formularioPreguntaSiete = PreguntaSiete(request.POST or None)
        if formularioPreguntaSiete.is_valid():
            datosSiete = formularioPreguntaSiete.cleaned_data

            respuesta = datosSiete.get("respuesta")
            fecha_registro_P07 = datosSiete.get("fecha_registro_P07")
            preguntaGuardada = True
            # Todo pasar la llave que tenemos del usuario
            # idEstudiante_global = globals()['idEstudiante_global']
            # print('*************** llave en la pregunta 7 ', idEstudiante_global)
            identificadorEstudianteSiete = Estudiante.objects.get(id=pk)
            objetoPregunta7 = Pregunta7.objects.create(respuesta=respuesta, fecha_registro_P07=fecha_registro_P07,
                                                       preguntaGuardada=preguntaGuardada,
                                                       identificadorEstudiante=identificadorEstudianteSiete,
                                                       respuestaCorrectaSiete=respuestaSiete)
            objetoPregunta7.save()
            # print('************el objeto del Pregunta 7 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 7 Exitosamente')
            # return render(request, "pregunta8.html", {})
            response = redirect('/pregunta8/' + str(pk))
            # print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formulario_PreguntaSiete": formularioPreguntaSiete,
        }

        return render(request, "pregunta7.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 7: {0}".format(e.with_traceback()))


# ********************* Pregunta 8
def preguntaOcho(request, pk):
    respuestaOcho = 'd'
    try:
        formularioPreguntaOcho = PreguntaOcho(request.POST or None)
        if formularioPreguntaOcho.is_valid():
            datosOcho = formularioPreguntaOcho.cleaned_data

            respuesta = datosOcho.get("respuesta")
            fecha_registro_P08 = datosOcho.get("fecha_registro_P08")
            preguntaGuardada = True
            # Todo pasar la llave que tenemos del usuario
            # idEstudiante_global = globals()['idEstudiante_global']
            # print('*************** llave en la pregunta 8 ', idEstudiante_global)
            identificadorEstudianteOcho = Estudiante.objects.get(id=pk)
            objetoPregunta8 = Pregunta8.objects.create(respuesta=respuesta, fecha_registro_P08=fecha_registro_P08,
                                                       preguntaGuardada=preguntaGuardada,
                                                       identificadorEstudiante=identificadorEstudianteOcho,
                                                       respuestaCorrectaOcho=respuestaOcho)
            objetoPregunta8.save()
            # print('************el objeto del Pregunta 8 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 8 Exitosamente')
            # return render(request, "pregunta9.html", {})
            response = redirect('/pregunta9/' + str(pk))
            # print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formulario_PreguntaOcho": formularioPreguntaOcho,
        }

        return render(request, "pregunta8.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 8: {0}".format(e.with_traceback()))


# ********************* Pregunta 9
def preguntaNueve(request, pk):
    respuestaNueve = 'c'
    try:
        formularioPreguntaNueve = PreguntaNueve(request.POST or None)
        if formularioPreguntaNueve.is_valid():
            datosNueve = formularioPreguntaNueve.cleaned_data

            respuesta = datosNueve.get("respuesta")
            fecha_registro_P09 = datosNueve.get("fecha_registro_P09")
            preguntaGuardada = True
            # Todo pasar la llave que tenemos del usuario
            # idEstudiante_global = globals()['idEstudiante_global']
            # print('*************** llave en la pregunta 9 ', idEstudiante_global)
            identificadorEstudianteNueve = Estudiante.objects.get(id=pk)
            objetoPregunta9 = Pregunta9.objects.create(respuesta=respuesta, fecha_registro_P09=fecha_registro_P09,
                                                       preguntaGuardada=preguntaGuardada,
                                                       identificadorEstudiante=identificadorEstudianteNueve,
                                                       respuestaCorrectaNueve=respuestaNueve)
            objetoPregunta9.save()
            # print('************el objeto del Pregunta 9 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 9 Exitosamente')
            # return render(request, "pregunta10.html", {})
            response = redirect('/pregunta10/' + str(pk))
            # print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formulario_PreguntaNueve": formularioPreguntaNueve,
        }

        return render(request, "pregunta9.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 9: {0}".format(e.with_traceback()))


# ********************* Pregunta 10
def preguntaDiez(request, pk):
    respuestaDiez = 'a'
    try:
        formularioPreguntaDiez = PreguntanDiez(request.POST or None)
        if formularioPreguntaDiez.is_valid():
            datosDiez = formularioPreguntaDiez.cleaned_data

            respuesta = datosDiez.get("respuesta")
            fecha_registro_P010 = datosDiez.get("fecha_registro_P010")
            preguntaGuardada = True
            # Todo pasar la llave que tenemos del usuario
            # idEstudiante_global = globals()['idEstudiante_global']
            # print('*************** llave en la pregunta 10 ', idEstudiante_global)
            identificadorEstudianteDiez = Estudiante.objects.get(id=pk)
            objetoPregunta10 = Pregunta10.objects.create(respuesta=respuesta, fecha_registro_P010=fecha_registro_P010,
                                                         preguntaGuardada=preguntaGuardada,
                                                         identificadorEstudiante=identificadorEstudianteDiez,
                                                         respuestaCorrectaDiez=respuestaDiez)

            objetoPregunta10.save()
            # print('************el objeto del Pregunta 10 se guardo con exito *******************')
            messages.success(request, 'Se Guardo la Pregunta 10 Exitosamente')
            response = redirect('/mensajeFinal/' + str(pk))
            # print('CAMILO ESTA LINEA ES CLAVE PARA EL EXITO')
            return response
        context = {
            "formulario_PreguntaDiez": formularioPreguntaDiez,
        }

        return render(request, "pregunta10.html", context)
    except ValueError as e:
        print("Error Guardado la Pregunta 10: {0}".format(e.with_traceback()))


def mensajeFinal(request, pk):
    # TODO SE CREAN LOS QUERYS
    try:

        # print('*************** llave en la pregunta 9 ', idEstudiante_global)
        identificadorEstudianteQuery = Estudiante.objects.get(id=pk)
        instance1 = Pregunta1.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        instance2 = Pregunta2.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        instance3 = Pregunta3.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        instance4 = Pregunta4.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        instance5 = Pregunta5.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        instance6 = Pregunta6.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        instance7 = Pregunta7.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        instance8 = Pregunta8.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        instance9 = Pregunta9.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        instance10 = Pregunta10.objects.filter(identificadorEstudiante_id=identificadorEstudianteQuery)
        valor = 0
        if (instance1.all().get().respuesta.__eq__(instance1.all().get().respuestaCorrectaUno)):
            uno = 10
            valor = (valor + uno)

        if (instance2.all().get().respuesta.__eq__(instance2.all().get().respuestaCorrectaDos)):
            uno = 10
            valor = (valor + uno)

        if (instance3.all().get().respuesta.__eq__(instance3.all().get().respuestaCorrectaTres)):
            uno = 10
            valor = (valor + uno)

        if (instance4.all().get().respuesta.__eq__(instance4.all().get().respuestaCorrectaCuatro)):
            uno = 10
            valor = (valor + uno)

        if (instance5.all().get().respuesta.__eq__(instance5.all().get().respuestaCorrectaCinco)):
            uno = 10
            valor = (valor + uno)

        if (instance6.all().get().respuesta.__eq__(instance6.all().get().respuestaCorrectaSeis)):
            uno = 10
            valor = (valor + uno)

        if (instance7.all().get().respuesta.__eq__(instance7.all().get().respuestaCorrectaSiete)):
            uno = 10
            valor = (valor + uno)

        if (instance8.all().get().respuesta.__eq__(instance8.all().get().respuestaCorrectaOcho)):
            uno = 10
            valor = (valor + uno)

        if (instance9.all().get().respuesta.__eq__(instance9.all().get().respuestaCorrectaNueve)):
            uno = 10
            valor = (valor + uno)

        if (instance10.all().get().respuesta.__eq__(instance10.all().get().respuestaCorrectaDiez)):
            uno = 10
            valor = (valor + uno)

        # print('*******************llego al ultimo mensaje')

        context = {
            "instance1": instance1,
            "instance2": str(valor),
        }
        return render(request, "mensajeFinal.html", context)
    except ValueError as e:
        print("Error Armando la Suma de Preguntas: {0}".format(e.with_traceback()))


def final(request):
    # //ip = request.body.find()
    # //print('Pruebas POST '+ str(ip))
    print('******************************* RETORNANDO EL REQUEST' + request.path)
    return render(request, "final.html", {})
