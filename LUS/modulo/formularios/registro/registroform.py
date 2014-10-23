#! /usr/bin/python
# -*- coding: UTF-8-*-
from django.db.models.fields import CharField

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
from django import forms
from modulo.models import *
from django.core.exceptions import ValidationError


def validate_username(value):
    username = unicode(value).encode("iso-8859-2", "replace")
    if Persona.objects.filter(username=username).exists():
        raise ValidationError(u'El ususario que ingresó ya se encuentra registrado en el sistema')

sexo = (('', ''),(1, 'Masculino'), (2, 'Femenino'))

class Registroform(forms.Form):
    nombre = forms.CharField(max_length=30, label=u"Primer nombre")
    apellido = forms.CharField(max_length=30, label=u"Primer apellido")
    sexo = forms.ChoiceField(choices=sexo, label=u"Sexo")
    usuario = forms.CharField(max_length=30, label=u"Nombre de Usuario", validators=[validate_username])
    contrasenia = forms.CharField(min_length=8, max_length=100,
                                  widget=forms.PasswordInput(render_value=False),
                                  label=u"Contraseñia")
    r_contrasenia = forms.CharField(min_length=8,
                                    max_length=100,
                                    widget=forms.PasswordInput(render_value=False),
                                    label=u"Confirmar contraseñia")
    email = forms.EmailField(max_length=200, min_length=5, label=u"Email")
    r_email = forms.EmailField(max_length=200, min_length=5, label=u"Confirmar email")

    def clean(self):
        """
            Función para vbalidar el formulario
        """

        usuario = self.cleaned_data.get('usuario', None)
        contrasenia = self.cleaned_data.get('contrasenia', None)
        r_contrasenia = self.cleaned_data.get('r_contrasenia', None)

        # validar usuername
        if User.objects.filter(username=usuario).exists():
            self._errors["usuario"] = u"El nombre del ususario " \
                                    u"ya se encuetra registrado"

        # validar email
        if Persona.objects.filter(username=usuario).exists():
            self._errors["email"] = u"El email ingresado " \
                                    u"ya se encuetra registrado"

        if contrasenia != r_contrasenia:
            self._errors["contrasenia"] = u"Datos no concuerdan", "ooo"
            self._errors["r_contrasenia"] = u"Datos no concuerdan"

        if contrasenia != r_contrasenia:
            self._errors["email"] = u"Datos no concuerdan"
            self._errors["r_email"] = u"Datos no concuerdan"

        return self.cleaned_data

    def get_nombre(self):
        return self.cleaned_data["nombre"]

    def get_apellido(self):
        return self.cleaned_data["apellido"]

    def get_sexo(self):
        return self.cleaned_data["sexo"]

    def get_usuario(self):
        return self.cleaned_data["usuario"]

    def get_contrasenia(self):
        return self.cleaned_data["contrasenia"]

    def get_r_contrasenia(self):
        return self.cleaned_data["r_contrasenia"]

    def get_email(self):
        return self.cleaned_data["email"]

    def get_r_email(self):
        return self.cleaned_data["r_email"]


    def __init__(self, *args, **kwargs):
        super(Registroform, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = "Nombre"
        self.fields['apellido'].widget.attrs['placeholder'] = "Apellido"
        self.fields['usuario'].widget.attrs['placeholder'] = "Usuario"
        self.fields['contrasenia'].widget.attrs['placeholder'] = "Contraseña"
        self.fields['r_contrasenia'].widget.attrs['placeholder'] = "Confirmar Contraseña"
        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['r_email'].widget.attrs['placeholder'] = "Confirmar Email"
        self.fields['sexo'].widget.attrs['class'] = "cmb-select selectpicker show-tick"
        self.fields['sexo'].widget.attrs['title'] = "Seleccione su Sexo"
        self.fields['sexo'].widget.attrs['data-live-search'] = True
