#! /usr/bin/python
# -*- coding: UTF-8 -*-
from django import template
from modulo.models import *
from LUS.settings import STATIC_URL

__author__ = 'Ivan'

register = template.Library()

@register.simple_tag(name='pintar_texto')
def pintar_texto(nombre):
    try:
        return ModuloTexto.objects.get(nombre=nombre).texto
    except ModuloTexto.DoesNotExist:
        ""


@register.simple_tag(name='pintar_imagen')
def pintar_imagen(nombre):
    return {'nombre': nombre, 'STATIC_URL': STATIC_URL}
register.inclusion_tag('tags/pintar_imagen.html')(pintar_imagen)


@register.simple_tag(name='ordenar_menu')
def ordenar_menu():
        menu = Menu.objects.filter(estado=True).order_by("orden")
        return {'menus': menu}

register.inclusion_tag('tags/llenar_menu.html')(ordenar_menu)