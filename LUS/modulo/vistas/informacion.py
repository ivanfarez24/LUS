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

from django.template.loader import render_to_string
from modulo.formularios.foros.foroForm import *
from django.core.urlresolvers import reverse

def nosotros(request):
    """
    Vista que presenta la lista de foros
    :param request:
    :return:
    """
    return render_to_response("acerca_de/acerca_nosotros.html",
                              {},
                              context_instance=RequestContext(request))

