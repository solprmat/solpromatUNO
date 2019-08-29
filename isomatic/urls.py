"""isomatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
# from django.urls import path

import isomaticAppWeb
from isomaticAppWeb import views as vista
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('isomaticAppWeb.urls')),
    # path('preguntaUno/', vista.preguntaUno),
    url(r'^admin/', admin.site.urls),
    url(r'^$', vista.inicio, name='inicio'),
    url(r'^tips/', tips, name='tips'),
    # url(r'^', include('isomaticAppWeb.urls', namespace='isomaticAppWeb')),
    url(r'^formularioUsuario/', vista.formularioUsuario, name='formularioUsuarioPrincipal'),
    # # url(r'^preguntaUno/', vista.preguntaUno, name='preguntaUno'),
    # # TODO TESTING
    url(r'^preguntaUno/(?P<pk>\d+)/$', vista.preguntaUno, name='preguntaUno'),
    url(r'^pregunta2/(?P<pk>\d+)/$', vista.preguntaDos, name='pregunta2'),
    url(r'^pregunta3/(?P<pk>\d+)/$', vista.preguntaTres, name='pregunta3'),
    url(r'^pregunta4/(?P<pk>\d+)/$', vista.preguntaCuatro, name='pregunta4'),
    url(r'^pregunta5/(?P<pk>\d+)/$', vista.preguntaCinco, name='pregunta5'),
    url(r'^pregunta6/(?P<pk>\d+)/$', vista.preguntaSeis, name='pregunta6'),
    url(r'^pregunta7/(?P<pk>\d+)/$', vista.preguntaSiete, name='pregunta7'),
    url(r'^pregunta8/(?P<pk>\d+)/$', vista.preguntaOcho, name='pregunta8'),
    url(r'^pregunta9/(?P<pk>\d+)/$', vista.preguntaNueve, name='pregunta9'),
    url(r'^pregunta10/(?P<pk>\d+)/$', vista.preguntaDiez, name='pregunta10'),
    url(r'^mensajeFinal/(?P<pk>\d+)/$', vista.mensajeFinal, name='mensajeFinal'),
    url(r'^final/', vista.final, name='final'),
    # # TODO PARA REDUX
    # url(r'^accounts/', include('registration.backends.default.urls')),

    # url('', TemplateView.as_view(template_name='forms/formularioEstudiante.html')),
    # url(r'^$', vista.formulario, name='formularioEstudiante'),
    # path('', include('vista.urls')),
    # path('admin/', admin.site.urls),
]
# TODO linea cuando es produccion
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#                       url(r'^__debug__/', include(debug_toolbar.urls)),
#
#                   ] + urlpatterns
