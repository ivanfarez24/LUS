#! /usr/bin/python
# -*- coding: UTF-8 -*-
from django.contrib import admin
from LUS.settings import *
from modulo.models import *

__author__ = 'Ivan'


def nombre_unicode(self):
    return u'%s' % self.nombre


def descripcion_unicode(self):
    return u'%s' % self.descripcion

ModuloTexto.__unicode__ = nombre_unicode
Menu.__unicode__ = nombre_unicode
Sexo.__unicode__ = nombre_unicode
Estado_civil.__unicode__ = nombre_unicode
Permiso.__unicode__ = nombre_unicode
Grupo.__unicode__ = nombre_unicode
Leccion.__unicode__ = nombre_unicode
Preguntas.__unicode__ = descripcion_unicode


class CommonMedia:
  js = (
      ('http://code.jquery.com/jquery-1.11.0.min.js',
       STATIC_URL+'ckeditor/ckeditor.js',
       STATIC_URL+'ckeditor/adapters/jquery.js',
       STATIC_URL+'js/consulta_editor.js')
  )
  css = {
    'all': (STATIC_URL + 'css/editor.css',)
  }


class AdminModuloTexto(admin.ModelAdmin):
    fields = ["nombre", 'texto', 'estado']
    list_display = ["id", "nombre", 'texto', 'estado']
    search_fields = ["nombre", 'texto', 'estado']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminMenu(admin.ModelAdmin):
    fields = ["nombre", 'imagen', 'url', 'orden', 'estado']
    list_display = ["nombre", 'imagen', 'url', 'orden', 'estado']
    search_fields = ["nombre", 'imagen', 'url', 'orden', 'estado']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminSexo(admin.ModelAdmin):
    fields = ['nombre', 'estado']
    list_display = ['nombre', 'estado']
    search_fields = ['nombre', 'estado']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminEstadoCivil(admin.ModelAdmin):
    fields = ['nombre', 'estado']
    list_display = ['nombre', 'estado']
    search_fields = ['nombre', 'estado']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminPermiso(admin.ModelAdmin):
    fields = ['nombre', 'descripcion', 'app', 'estado']
    list_display = ['nombre', 'descripcion', 'app', 'estado']
    search_fields = ['nombre', 'descripcion', 'app', 'estado']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminGrupo(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion')
    filter_horizontal = ('permisos',)
    list_display = ['nombre', 'estado']
    search_fields = ['nombre', 'estado']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminPersona(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion',
                'groups', 'user_permissions')

    filter_horizontal = ('permisos', 'grupo')

    list_display = ['username', 'nombre', 'cedula', 'estado_civil', 'is_active']
    search_fields = ['username', 'nombre', 'cedula', 'estado_civil', 'is_active']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminLeccion(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion')

    list_display = ['id', 'nombre']
    search_fields = ['id', 'nombre']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminPreguntas(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion')

    #filter_horizontal = ('respuestas',)

    list_display = ['id', 'leccion', 'descripcion']
    search_fields = ['id', 'leccion', 'descripcion']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


admin.site.register(ModuloTexto, AdminModuloTexto, Media=CommonMedia)
admin.site.register(Menu, AdminMenu)
admin.site.register(Sexo, AdminSexo)
admin.site.register(Estado_civil, AdminEstadoCivil)
admin.site.register(Permiso, AdminPermiso)
admin.site.register(Grupo, AdminGrupo)
admin.site.register(Persona, AdminPersona)
admin.site.register(Leccion, AdminLeccion)
#admin.site.register(Preguntas, AdminPreguntas)
