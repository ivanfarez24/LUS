#! /usr/bin/python
# -*- coding: UTF-8-*-
__author__ = 'Ivancho'
from django.template import RequestContext
from django.shortcuts import render_to_response
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
from modulo.formularios.registro.registroform import *
from django.contrib.auth import login, authenticate, logout
from modulo.models import *


def registrarse(request):
    form = Registroform()
    #if request.user.is_authenticated() == False:
    if request.method == "POST":
        form = Registroform(request.POST)
        if form.is_valid():
            persona = Persona()
            persona.first_name = form.get_nombre()
            persona.last_name = form.get_apellido()
            persona.username = form.get_usuario()
            persona.password = form.get_contrasenia()
            persona.sexo = form.get_sexo()
            persona.usuario_creacion = 'sistema'
            persona.fecha_creacion = datetime.datetime.now()
            persona.email = form.get_email()
            persona.save()
        else:
            messages.error(request, u"Por favor verificar los datos requeridos")

    return render_to_response("registro/registro.html", {"form": form},
                              context_instance=RequestContext(request))

    #else:
    #    return HttpResponseRedirect(reverse("administracion"))


def salir(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
