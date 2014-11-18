#! /usr/bin/python
# -*- coding: UTF-8 -*-
from django import template
from modulo.models import *
from LUS.settings import STATIC_URL
from LUS.templatetags.decorators import condition_tag
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
        menu = Menu.objects.filter(estado=True, grupo_menu=None).order_by("orden")
        return {'menus': menu}
register.inclusion_tag('tags/llenar_menu.html')(ordenar_menu)


@register.tag
@condition_tag
def if_puede_dar_like(request, foro_comentario_id):
    if not PersonaVotoComentario.objects.filter(foro_comentario_id=foro_comentario_id,
                                                persona_id=request.user.id).exists():
        return True
    else:
        return False