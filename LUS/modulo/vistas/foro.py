#! /usr/bin/python
# -*- coding: UTF-8-*-
__author__ = 'Ivancho'

from django.template import RequestContext
from django.shortcuts import render_to_response
from modulo.models import *
import json
from django.http import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template.loader import render_to_string
from modulo.formularios.foros.foroForm import *
from django.core.urlresolvers import reverse

def foro(request):
    """
    Vista que presenta la lista de foros
    :param request:
    :return:
    """
    foros = Foro.objects.filter(estado=True)
    return render_to_response("foro/foros.html",
                              {"foros": foros},
                              context_instance=RequestContext(request))

@csrf_exempt
@login_required()
def agregar_foro(request):
    """
    Vista que presenta la lista de foros
    :param request:
    :return:
    """
    foro = Foroform()
    if request.method == "POST":
        foro = Foroform(request.POST)
        if foro.is_valid():
            foro_obj = Foro()
            foro_obj.tema = foro.get_tema()
            foro_obj.pregunta = foro.get_pregunta()
            foro_obj.persona_id = request.user.id
            foro_obj.save()
            messages.success(request, u"Se ha agregado exitosamente el tema de foro")
            return HttpResponseRedirect(reverse("foro"))
        else:
            messages.error(request, u"Por favor ingrese los campos obligatorios")

    return render_to_response("foro/agregar_foro.html",
                              {"foro": foro},
                              context_instance=RequestContext(request))

@csrf_exempt
@login_required()
def editar_foro(request, id):
    """
    Vista que presenta la lista de foros
    :param request:
    :return:
    """
    foro = Foro.objects.get(id=id)
    foro_form = Foroform(initial={"tema": foro.tema, "pregunta": foro.pregunta})

    if request.method == "POST":
        foro_form = Foroform(request.POST)
        if foro_form.is_valid():
            foro.tema = foro_form.get_tema()
            foro.pregunta = foro_form.get_pregunta()
            foro.fecha_actualizacion = datetime.datetime.now()
            foro.usuario_actualizacion = request.user.username
            foro.save()
            messages.success(request, u"Se ha editado exitosamente el tema de foro")
            return HttpResponseRedirect(reverse("foro"))
        else:
            messages.error(request, u"Por favor ingrese los campos obligatorios")

    return render_to_response("foro/editar_foro.html",
                              {"foro": foro_form},
                              context_instance=RequestContext(request))


@csrf_exempt
@login_required()
def responder_foro(request, id):
    """
    Vista que presenta el foro y sus respuestas
    :param request:
    :return:
    """
    try:
        foro = Foro.objects.get(id=id)
        now = datetime.datetime.now()
        foro.numero_visitas += 1
        foro.save()
        if request.is_ajax():
            if request.user.is_authenticated():
                comentario_foro = request.POST.get("respuesta", "")
                usuario = request.user.username
                persona = Persona.objects.get(id=request.user.id)
                comentario = ForoComentarios()
                comentario.comentario = comentario_foro
                comentario.foro = foro
                comentario.usuario_creacion = usuario
                comentario.persona = persona
                comentario.fecha_creacion = now
                if comentario_foro != "":
                    comentario.save()

                html = render_to_string('tags/foro/comentario.html', {'foro': foro, 'obj': comentario, "request": request})
                return HttpResponse(html)

        return render_to_response("foro/resp_foro.html",
                              {"foro": foro, "id": id},
                              context_instance=RequestContext(request))
    except Foro.DoesNotExist:
        return HttpResponseRedirect(reverse("foro"))


@csrf_exempt
@login_required()
def editar_comentario(request):
    """
    Vista que presenta el foro y sus respuestas
    :param request:
    :return:
    """
    try:
        if request.is_ajax():
            comentario_foro = request.POST.get("respuesta", "")
            id_comentario = request.POST.get("id_comentario", "")

            usuario = request.user.username
            persona = Persona.objects.get(id=request.user.id)

            if ForoComentarios.objects.filter(persona=persona, id=id_comentario).exists():
                comentario = ForoComentarios.objects.get(id=id_comentario, persona=persona)
                comentario.comentario = comentario_foro
                comentario.usuario_actualizacion = usuario
                comentario.fecha_actualizacion = datetime.datetime.now()
                if comentario_foro != "":
                    comentario.save()
                else:
                    messages.error(request, "El comentario no se guardó por estar vacio")

                respuesta = ({"status": 1})
            else:
                respuesta = ({"status": 0})

        else:
            respuesta = ({"status": 0})

        resultado = json.dumps(respuesta)
        return HttpResponse(resultado, mimetype='application/json')

    except Foro.DoesNotExist:
        return HttpResponseRedirect(reverse("foro"))


@csrf_exempt
@login_required()
def eliminar_comentario_foro(request, id_foro, id_coment):
    """
    Vista que presenta el foro y sus respuestas
    :param request:
    :return:
    """
    try:
        now = datetime.datetime.now()
        foro_comentario_id = id_coment
        usuario = request.user.username
        if ForoComentarios.objects.filter(id=foro_comentario_id, persona_id=request.user.id).exists():
            comentario = ForoComentarios.objects.get(id=foro_comentario_id, persona_id=request.user.id)
            comentario.fecha_actualizacion = now
            comentario.estado = False
            comentario.usuario_actualizacion = usuario
            comentario.save()
            return HttpResponseRedirect(reverse('responder_foro', args=[id_foro]))
        else:
            messages.error(request, u"No tiene permisos para realizar esta operación")
            return HttpResponseRedirect(reverse('responder_foro', args=[id_foro]))
    except Foro.DoesNotExist:
        return HttpResponseRedirect(reverse('responder_foro', args=[id_foro]))


@csrf_exempt
def like_comentario(request):
    if request.is_ajax():

        if request.user.is_authenticated():

            like = int(request.POST.get("opt", 1))
            foro_comentario_id = request.POST.get("id", 0)
            if like == 1:  # like
                if not PersonaVotoComentario.objects.filter(foro_comentario_id=foro_comentario_id,
                                                            persona_id=request.user.id).exists():
                    persona_voto_comentario = PersonaVotoComentario()
                    persona_voto_comentario.foro_comentario_id = foro_comentario_id
                    persona_voto_comentario.persona_id = request.user.id
                    persona_voto_comentario.estado = True
                    persona_voto_comentario.fecha_creacion = datetime.datetime.now()
                    persona_voto_comentario.usuario_creacion = request.user.username
                    persona_voto_comentario.save()
                    respuesta = ({"status": 1})
                else:
                    respuesta = ({"status": 0})
            else:  # unlike
                if PersonaVotoComentario.objects.filter(foro_comentario_id=foro_comentario_id,
                                                        persona_id=request.user.id).exists():
                    persona_voto_comentario = PersonaVotoComentario.objects.get(foro_comentario_id=foro_comentario_id,
                                                                                persona_id=request.user.id)
                    persona_voto_comentario.delete()
                    respuesta = ({"status": 1})
                else:
                    respuesta = ({"status": 0})
        else:
            respuesta = ({"status": 0})
    else:
        respuesta = ({"status": 0})

    resultado = json.dumps(respuesta)
    return HttpResponse(resultado, mimetype='application/json')


@csrf_exempt
def get_num_votos(request):
    if request.is_ajax():

        if request.user.is_authenticated():
            foro_comentario_id = request.POST.get("id", 0)
            num_votos = len(PersonaVotoComentario.objects.filter(foro_comentario_id=foro_comentario_id))
            respuesta = ({"status": 1, "num_votos": num_votos})
        else:
            respuesta = ({"status": 0})
    else:
        respuesta = ({"status": 0})

    resultado = json.dumps(respuesta)
    return HttpResponse(resultado, mimetype='application/json')


@csrf_exempt
def eliminar_foro(request, id):
    if request.user.is_authenticated():
        foro_id = id
        try:
            foro = Foro.objects.get(id=foro_id, persona_id=request.user.id)
            foro.estado = False
            foro.save()
            messages.success(request, u"Se ha eliminado exitosamente el tema de foro")
            return HttpResponseRedirect(reverse("foro"))
        except (Foro.DoesNotExist, IndexError) as e:
            messages.error(request, u"Error recurso no encontrado")
            return HttpResponseRedirect(reverse("foro"))
    else:
        messages.error(request, u"No tiene permisos para realizar esta operación")
        return HttpResponseRedirect(reverse("foro"))