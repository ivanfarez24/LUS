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


def capitulos(request):
    """
    Vista que presenta la lista de foros
    :param request:
    :return:
    """
    capitulos = Capitulos.objects.filter(estado=True)
    return render_to_response("capitulos/lista_capitulos.html",
                              {"capitulos": capitulos},
                              context_instance=RequestContext(request))


def leer_capitulo(request, id):
    """
    Vista que presenta el capítulo seleccionado
    por el usuario
    :param request:
    :return:
    """
    sub_cap = SubCapitulos.objects.get(id=id)
    return render_to_response("capitulos/capitulo_general.html",
                              {"sub_cap": sub_cap},
                              context_instance=RequestContext(request))