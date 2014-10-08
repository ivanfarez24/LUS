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


def login(request):
    loginform = Loginform()
    return render_to_response("login/login.html",
        {'form': loginform }, context_instance=RequestContext(request))