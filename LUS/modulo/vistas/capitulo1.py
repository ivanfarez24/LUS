#! /usr/bin/python
# -*- coding: UTF-8-*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import *
import datetime
from django.template.loader import render_to_string

__author__ = 'Ivan'


@csrf_exempt
def capitulo1_view(request):
    if request.is_ajax():
        q = request.POST.get("capt", "")
        #html = render_to_string('frontend/scroll.html', {'dishes': dishes})
        if q == "1.1" or q == "0":
            html = render_to_response('capitulo1/subcapitulo/home.html', {'subcap': 'subcap1.1',
                                                                          'img': 'antena.png',
                                                                          'before': '1.1',
                                                                          'next': '1.2'}, context_instance=RequestContext(request))
        elif q == "1.2":
            html = render_to_response('capitulo1/subcapitulo/home.html', {'subcap': 'subcap1.2',
                                                                          'img': 'phone_lock.png',
                                                                          'before': '1.1',
                                                                          'next': '1.3'}, context_instance=RequestContext(request))
        elif q == "1.3":
            html = render_to_string('capitulo1/subcapitulo/home.html', {'subcap': 'subcap1.3',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '1.2',
                                                                        'next': '1.4'}, context_instance=RequestContext(request))
        elif q == "1.4":
            html = render_to_string('capitulo1/subcapitulo/home.html', {'subcap': 'subcap1.4',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '1.3',
                                                                        'next': '1.4.1'}, context_instance=RequestContext(request))
        elif q == "1.4.1":
            html = render_to_string('capitulo1/subcapitulo/home.html', {'subcap': 'subcap1.4.1',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '1.4',
                                                                        'next': '1.4.2'}, context_instance=RequestContext(request))
        elif q == "1.4.2":
            html = render_to_string('capitulo1/subcapitulo/home.html', {'subcap': 'subcap1.4.2',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '1.4.1',
                                                                        'next': '1.4.3'}, context_instance=RequestContext(request))
        elif q == "1.4.3":
            html = render_to_string('capitulo1/subcapitulo/home.html', {'subcap': 'subcap1.4.3',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '1.4.2',
                                                                        'next': '1.4.4'}, context_instance=RequestContext(request))
        elif q == "1.4.4":
            html = render_to_string('capitulo1/subcapitulo/home.html', {'subcap': 'subcap1.4.4',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '1.4.3',
                                                                        'next': '1.4.5'}, context_instance=RequestContext(request))
        elif q == "1.4.5":
            html = render_to_string('capitulo1/subcapitulo/home.html', {'subcap': 'subcap1.4.5',
                                                                        'img': 'arquitectura_umts.png',
                                                                        'before': '1.4.4',
                                                                        'next': '1.4.6'}, context_instance=RequestContext(request))
        else:
            html = ""
        return HttpResponse(html)
    return render_to_response("capitulo1/home.html",context_instance=RequestContext(request))

