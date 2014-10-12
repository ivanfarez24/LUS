#! /usr/bin/python
# -*- coding: UTF-8 -*-
from django import template
from modulo.models import *
from LUS.settings import STATIC_URL
from django.utils.html import *

__author__ = 'Ivancho'

register = template.Library()


@register.simple_tag(name='validar_respuesta')
def validar_respuesta(lista_c, lista_inc, id):
    respuesta = Respuestas.objects.get(id=id)
    if id in lista_c:
        return format_html('<span class="respuesta respuesta-acierto"><i class="fa fa-check-square-o"></i></span>')

    elif id in lista_inc:
        return format_html('<span class="respuesta respuesta-errada"><i class="fa fa-times-circle"></i></span>')

    elif respuesta.puntuacion > 0:
        return format_html('<span class="respuesta respuesta-vacia"><i class="fa fa-times-circle"></i>'
                           'Esta era la respuesta correcta</span>')

    else:
        return ""
