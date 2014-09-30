#! /usr/bin/python
# -*- coding: UTF-8-*-
__author__ = 'Ivan'
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import *
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q

from django.db.models import Sum
import operator
from django.db.models import F
from django.forms.formsets import formset_factory


@csrf_exempt
def capitulo2_view(request):
    if request.is_ajax():
        q = request.POST.get("capt", "")
        #html = render_to_string('frontend/scroll.html', {'dishes': dishes})
        print "XXXXXXXXXXXXX"
        print q
        if q == "2.1" or q == "0":
            html = render_to_response('capitulo2/subcapitulo/home.html', {'subcap': 'subcap2.1',
                                                                          'img': 'antena.png',
                                                                          'before': '2.1',
                                                                          'next': '2.2'}, context_instance=RequestContext(request))
        elif q == "2.2":
            html = render_to_response('capitulo2/subcapitulo/home.html', {'subcap': 'subcap2.2',
                                                                          'img': 'phone_lock.png',
                                                                          'before': '2.1',
                                                                          'next': '2.3'}, context_instance=RequestContext(request))
        elif q == "2.3":
            html = render_to_string('capitulo2/subcapitulo/home.html', {'subcap': 'subcap2.3',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '2.2',
                                                                        'next': '2.4'}, context_instance=RequestContext(request))
        elif q == "2.4":
            html = render_to_string('capitulo2/subcapitulo/home.html', {'subcap': 'subcap2.4',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '2.3',
                                                                        'next': '2.4.1'}, context_instance=RequestContext(request))
        elif q == "2.4.1":
            html = render_to_string('capitulo2/subcapitulo/home.html', {'subcap': 'subcap2.4.1',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '2.4',
                                                                        'next': '2.4.2'}, context_instance=RequestContext(request))
        elif q == "2.4.2":
            html = render_to_string('capitulo1/subcapitulo/home.html', {'subcap': 'subcap2.4.2',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '2.4.1',
                                                                        'next': '2.4.3'}, context_instance=RequestContext(request))
        elif q == "2.4.3":
            html = render_to_string('capitulo1/subcapitulo/home.html', {'subcap': 'subcap2.4.3',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '2.4.2',
                                                                        'next': '-1'}, context_instance=RequestContext(request))
        else:
            html = ""
        return HttpResponse(html)
    return render_to_response("capitulo2/home.html",context_instance=RequestContext(request))
