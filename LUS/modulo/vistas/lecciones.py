#! /usr/bin/python
# -*- coding: UTF-8-*-
__author__ = 'Ivancho'

from django.template import RequestContext
from django.shortcuts import render_to_response
from modulo.models import *
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


@csrf_exempt
def lecciones_lista(request):
    lecciones = Leccion.objects.filter(estado=True).order_by("-numero")

    return render_to_response("lecciones/lecciones.html",{'lecciones':lecciones},context_instance=RequestContext(request))

@csrf_exempt
def leccion(request, id):
    cont = 0  # Cuenta la puntuación total de la lección
    lista_ids_resp_correc = []  # Listas de los ids de las resp correctas
    lista_ids_resp_inco = []  # Listas de los ids de las resp correctas
    try:
        leccion = Leccion.objects.get(id=id)
        if request.method == "POST":
            for obj in leccion.get_preguntas():
                for obj_res in obj.get_respuestas():
                    resp = request.POST.get(str(obj.id)+"-"+str(obj_res.id))
                    if resp is not None:
                        if obj_res.puntuacion > 0:
                            cont += 1
                            lista_ids_resp_correc.append(obj_res.id)
                        else:
                            lista_ids_resp_inco.append(obj_res.id)

            return render_to_response("lecciones/leccion_resultado.html",
                                      {"leccion": leccion,
                                       "lista_correcta": lista_ids_resp_correc,
                                       "lista_incorrecta": lista_ids_resp_inco,
                                       "puntuacion": cont},
                                      context_instance=RequestContext(request))
    except Leccion.DoesNotExist:
        leccion = None
    return render_to_response("lecciones/leccion.html",
                              {"leccion": leccion,
                               "lista_correcta": lista_ids_resp_correc,
                               "lista_incorrecta": lista_ids_resp_inco,
                               "puntuacion": cont},
                              context_instance=RequestContext(request))

