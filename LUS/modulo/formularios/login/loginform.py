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


class Loginform(forms.Form):
    usuario = forms.CharField(max_length=30)
    contrasenia = forms.CharField(max_length=50)


    def get_user(self):
        return self.cleaned_data["usuario"]

    def get_pass(self):
        return self.cleaned_data["contrasenia"]
    """
    def __init__(self, *args, **kwargs):
        super(Loginform, self).__init__(*args, **kwargs)
        self.fields['contrasenia'].widget.attrs[''] = "yyyy-mm-dd"
    """