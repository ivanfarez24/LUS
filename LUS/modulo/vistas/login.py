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
from modulo.formularios.login.loginform import *
from django.contrib.auth import login, authenticate, logout


def login_view(request):
    if request.user.is_authenticated() == False:
        siguiente = request.GET.get("next", "")
        if request.method == "POST":
            form = Loginform(request.POST)
            if form.is_valid():
                username = form.cleaned_data["usuario"]
                password = form.cleaned_data["contrasenia"]
                user = authenticate(username=username, password=password, is_active=True)
                if user is not None:
                    if user.is_active:
                        login(request, user)

                        if siguiente != "":
                            return HttpResponseRedirect(siguiente)
                        else:
                            return HttpResponseRedirect(reverse("inicio_view"))
                    else:
                        messages.info(request, u"El usuario está inactivo comunicarse con el administrador del sistema")
                        return HttpResponseRedirect(reverse("login"))
                else:
                    messages.error(request, u"Ha ingresado un usuario o contraseña incorrecta")
                    return HttpResponseRedirect(reverse("login"))
            else:
                form = Loginform(initial={"next": siguiente})
                messages.error(request, u"Por favor para iniciar sesión debe ingresar su usuario y su clave.")
                return render_to_response("login/login.html", {"form": form},context_instance=RequestContext(request))
        else:
            form = Loginform(initial={"next": siguiente})
            return render_to_response("login/login.html", {"form": form},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse("inicio_view"))

def salir(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

