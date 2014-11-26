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
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@+"
    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    return p


def generar_cont_temp(longitud=8):
    valores = "0123456789"
    p = r""
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
                persona.set_password(form.get_contrasenia())
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
        messages.success(request, u"Su cuenta ya esta activada")
        return HttpResponseRedirect(reverse('inicio_view'))


@csrf_exempt
@transaction.commit_on_success
def recuperar_contrasenia(request):
    form = RecuperarContraseniaForm()
    if not request.user.is_authenticated():
        if request.method == "POST":
            form = RecuperarContraseniaForm(request.POST)
            if form.is_valid():
                try:
                    email = form.get_email()
                    if Persona.objects.filter(email=email).exists():
                        persona = Persona.objects.filter(email=email).order_by("id")[0]
                        contrasenia_temp = str(generar_cont_temp(8)).replace(" ", "")
                        persona.set_password(contrasenia_temp)
                        persona.usuario_creacion = 'sistema'
                        persona.fecha_actualizacion = datetime.datetime.now()
                        persona.save()

                        # Mailing
                        mensaje = render_to_string("mailings/recuperar_contrasenia.html",
                                                   {"persona": persona,
                                                    "contrasenia_temp": contrasenia_temp},
                                                   context_instance=RequestContext(request))
                        subject, \
                        from_email, \
                        to = u'Recuperar contraseña', u'LUS'+'<'+'info@lusonline.net'+'>', persona.email
                        msg = EmailMessage(subject, mensaje, from_email, [to])
                        msg.content_subtype = "html"  # Main content is now text/html
                        msg.send()
                        messages.success(request, u"Se ha enviado un mensaje a su correo electrónico, "
                                                  u"con su contraseña temporal.")

                except Persona.DoesNotExist:
                    transaction.rollback()
                return HttpResponseRedirect(reverse('inicio_view'))
            else:
                messages.error(request, u"El correo que ingresó no se encuentra registrado en el sistema")

    return render_to_response("login/recuperar_contrasenia.html", {"form": form},
                              context_instance=RequestContext(request))


@csrf_exempt
@transaction.commit_on_success
@login_required()
def cambiar_contrasenia(request):
    form = CamnbiarContraseniaForm()
    if request.method == "POST":
        form = CamnbiarContraseniaForm(request.POST)
        if form.is_valid():
            nueva_cont = form.get_contrasenia_nueva()
            persona = Persona.objects.get(id=request.user.id)
            persona.set_password(nueva_cont)
            persona.usuario_actualizacion = request.user.username
            persona.fecha_actualizacion = datetime.datetime.now()
            persona.save()
            messages.success(request, u"Se ha cambiado con éxito su contraseña")

            return HttpResponseRedirect(reverse('inicio_view'))
        else:
            messages.error(request, u"No coinciden las contraseñas")

    return render_to_response("login/cambiar_contrasenia.html", {"form": form},
                              context_instance=RequestContext(request))
