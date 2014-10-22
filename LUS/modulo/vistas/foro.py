#! /usr/bin/python
# -*- coding: UTF-8-*-
__author__ = 'Ivancho'

from django.template import RequestContext
from django.shortcuts import render_to_response
from modulo.models import *
import json
from django.http import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q

from django.db.models import Sum
import operator
from django.db.models import F
from django.forms.formsets import formset_factory
from django.template.loader import render_to_string


def foro(request):
    """
    Vista que presenta la lista de foros
    :param request:
    :return:
    """
    foros = Foro.objects.filter(estado=True)
    return render_to_response("foro/foros.html",
                              {"foros": foros},
                              context_instance=RequestContext(request))

@csrf_exempt
def responder_foro(request, id):
    """
    Vista que presenta el foro y sus respuestas
    :param request:
    :return:
    """
    try:
        foro = Foro.objects.get(id=id)
        now = datetime.datetime.now()

        if request.is_ajax():
            comentario_foro = request.POST.get("respuesta", "")
            usuario = request.user.username
            persona = Persona.objects.get(id=request.user.id)
            comentario = ForoComentarios()
            comentario.comentario = comentario_foro
            comentario.foro = foro
            comentario.usuario_creacion = usuario
            comentario.persona = persona
            comentario.fecha_creacion = now
            if comentario_foro != "":
                comentario.save()

            html = render_to_string('tags/foro/comentario.html', {'obj': comentario})
            return HttpResponse(html)

        return render_to_response("foro/resp_foro.html",
                              {"foro": foro, "id": id},
                              context_instance=RequestContext(request))
    except Foro.DoesNotExist:
        pass