from django.conf.urls import url

from isomaticAppWeb.views import formularioUsuario, preguntaUno, preguntaDos, preguntaTres, preguntaCuatro, preguntaCinco, \
    preguntaSeis, preguntaSiete, preguntaOcho, preguntaNueve, preguntaDiez, mensajeFinal, final

urlpatterns = [
    url(r'^formularioUsuario/', formularioUsuario, name='formularioUsuario'),
    # url(r'^preguntaUno/', vista.preguntaUno, name='preguntaUno'),
    # TODO TESTING
    url(r'^preguntaUno/', preguntaUno, name='preguntaUno'),
    url(r'^pregunta2/', preguntaDos, name='pregunta2'),
    url(r'^pregunta3/', preguntaTres, name='pregunta3'),
    url(r'^pregunta4/', preguntaCuatro, name='pregunta4'),
    url(r'^pregunta5/', preguntaCinco, name='pregunta5'),
    url(r'^pregunta6/', preguntaSeis, name='pregunta6'),
    url(r'^pregunta7/', preguntaSiete, name='pregunta7'),
    url(r'^pregunta8/', preguntaOcho, name='pregunta8'),
    url(r'^pregunta9/', preguntaNueve, name='pregunta9'),
    url(r'^pregunta10/', preguntaDiez, name='pregunta10'),
    url(r'^mensajeFinal/', mensajeFinal, name='mensajeFinal'),
    url(r'^final/', final, name='final'),

]
