#! /usr/bin/python
# -*- coding: UTF-8-*-

__author__ = 'Ivancho'

from django import forms


class Loginform(forms.Form):
    usuario = forms.CharField(max_length=30)
    contrasenia = forms.CharField(widget=forms.PasswordInput(render_value=False), label="Clave")


    def get_user(self):
        return self.cleaned_data["usuario"]

    def get_pass(self):
        return self.cleaned_data["contrasenia"]

    def __init__(self, *args, **kwargs):
        super(Loginform, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs['placeholder'] = "Usuario"
        self.fields['contrasenia'].widget.attrs['placeholder'] = "Contraseña"
