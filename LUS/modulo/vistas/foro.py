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


def responder_foro(request, id):
    """
    Vista que presenta el foro y sus respuestas
    :param request:
    :return:
    """
    try:
        foro = Foro.objects.get(id=id)
        return render_to_response("foro/resp_foro.html",
                              {"foros": foros},
                              context_instance=RequestContext(request))
    except Foro.DoesNotExist:
        pass