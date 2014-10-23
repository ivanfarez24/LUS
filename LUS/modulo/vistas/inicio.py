#! /usr/bin/python
# -*- coding: UTF-8-*-
__author__ = 'Ivan'
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from modulo.models import *
from django.db.models import Sum
import operator
from django.db.models import F
from django.forms.formsets import formset_factory

def inicio_view(request):

    modulo1 = None
    modulo2 = None
    modulo3 = None

    try:
        modulo1 = ModuloTexto.objects.get(nombre='modulo1')
        modulo2 = ModuloTexto.objects.get(nombre='modulo2')
        modulo3 = ModuloTexto.objects.get(nombre='modulo3')
    except:
        pass

    datos = {
        'modulo1': modulo1,
        'modulo2': modulo2,
        'modulo3': modulo3
    }
    return render_to_response("inicio/inicio.html",datos,context_instance=RequestContext(request))