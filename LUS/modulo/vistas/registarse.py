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
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from random import choice
from django.db import transaction

def generar_clave(longitud=18):
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    return p


@csrf_exempt
@transaction.commit_on_success
def registrarse(request):
    form = Registroform()
    #if request.user.is_authenticated() == False:
    if request.method == "POST":
        form = Registroform(request.POST)
        if form.is_valid():
            try:
                persona = Persona()
                persona.first_name = form.get_nombre()
                persona.last_name = form.get_apellido()
                persona.username = form.get_usuario()
                persona.password = form.get_contrasenia()
                persona.sexo = Sexo.objects.get(id=form.get_sexo())
                persona.clave_temp = generar_clave(18)

                persona.usuario_creacion = 'sistema'
                persona.fecha_creacion = datetime.datetime.now()
                persona.email = form.get_email()
                persona.is_active = False
                persona.save()
                # Mailing
                mensaje = render_to_string("mailings/registro.html",
                                           {"persona": persona}, context_instance=RequestContext(request))
                subject, \
                from_email, \
                to = u'Confirmación de Cuenta', u'LUS'+'<'+'info@lusonline.net'+'>', persona.email
                msg = EmailMessage(subject, mensaje, from_email, [to])
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
                messages.success(request, u"Se ha enviado un mensaje a su correo electrónico, "
                                          u"por favor confirme su registro.")
            except Persona.DoesNotExist:
                transaction.rollback()
            return HttpResponseRedirect(reverse('inicio_view'))
        else:
            messages.error(request, u"Por favor verificar los datos requeridos")

    return render_to_response("registro/registro.html", {"form": form},
                              context_instance=RequestContext(request))

    #else:
    #    return HttpResponseRedirect(reverse("administracion"))


def activar_cuenta(request, id, clave):
    if Persona.objects.filter(id=id, is_active=False).exists():
        persona = Persona.objects.get(id=id)
        if persona.clave_temp == clave:
            persona.is_active = True
            persona.fecha_actualizacion = datetime.datetime.now()
            persona.usuario_actualizacion = 'sistema'
            persona.save()
            messages.success(request, u"Su cuenta ha sido activada exitosamente")
        return HttpResponseRedirect(reverse('inicio_view'))
    else:
        return HttpResponseRedirect(reverse('inicio_view'))


def salir(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
