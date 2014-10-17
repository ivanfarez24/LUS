#! /usr/bin/python
# -*- coding: UTF-8 -*-
from django.contrib import admin
from LUS.settings import *
from modulo.models import *
from django.forms.models import BaseInlineFormSet

__author__ = 'Ivan'


def nombre_unicode(self):
    return u'%s' % self.nombre


def descripcion_unicode(self):
    return u'%s' % self.descripcion


def tema_unicode(self):
    return u"%s" % self.tema


def subcap_unicode(self):
    return u"%s - %s" % self.capitulo.nombre, self.titulo

ModuloTexto.__unicode__ = nombre_unicode
Menu.__unicode__ = nombre_unicode
Sexo.__unicode__ = nombre_unicode
Estado_civil.__unicode__ = nombre_unicode
Permiso.__unicode__ = nombre_unicode
Grupo.__unicode__ = nombre_unicode
Leccion.__unicode__ = nombre_unicode
Preguntas.__unicode__ = descripcion_unicode
Foro.__unicode__ = tema_unicode
Capitulos.__unicode__ = nombre_unicode

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


class ModuloInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super(ModuloInlineFormSet, self).clean()

        for form in self.forms:
            if not form.is_valid():
                return #other errors exist, so don't bother
            if form.cleaned_data.get('DELETE'):
                pass
                # Hacer el borrado de la tabla grupo_permisos y
                # de la tabla persona permisos
                # Cojiendo los datos de la base del cliente


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
    fields = ["nombre", 'grupo_menu', 'imagen', 'url', 'orden', 'estado']
    list_display = ["nombre", 'grupo_menu', 'imagen', 'url', 'orden', 'estado']
    search_fields = ["nombre", 'grupo_menu', 'imagen', 'url', 'orden', 'estado']

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


class PreguntasInline(admin.TabularInline):
    model = Preguntas
    extra = 2
    formset = ModuloInlineFormSet
    exclude = ["fecha_actualizacion", "usuario_actualizacion", "fecha_creacion", "usuario_creacion"]


class AdminLeccion(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion')

    inlines = (PreguntasInline,)

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


class RespuestasInline(admin.TabularInline):
    model = Respuestas
    extra = 2
    formset = ModuloInlineFormSet
    exclude = ["fecha_actualizacion", "usuario_actualizacion", "fecha_creacion", "usuario_creacion"]


class AdminPreguntas(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion')

    inlines = (RespuestasInline,)

    list_display = ['id', 'descripcion', 'leccion']
    search_fields = ['id', 'descripcion', 'leccion']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminForo(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion')

    list_display = ['id', 'tema', 'pregunta', 'numero_visitas']
    search_fields = ['id', 'tema', 'pregunta', 'numero_visitas']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminForoRespuesta(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion')

    list_display = ['id', 'persona', 'comentario', 'numero_votos']
    search_fields = ['id', 'persona', 'comentario', 'numero_votos']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminCapitulo(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion')

    list_display = ['id', 'nombre', 'descripcion', 'imagen']
    search_fields = ['id', 'nombre', 'descripcion', 'imagen']

    def save_model(self, request, obj, form, change):
        if not obj.usuario_creacion:
            obj.usuario_creacion = request.user.username
        obj.usuario_actualizacion = request.user.username
        if not obj.fecha_creacion:
            obj.fecha_creacion = datetime.datetime.now()
        obj.fecha_actualizacion = datetime.datetime.now()
        obj.save()


class AdminSubcapitulo(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_actualizacion',
                'fecha_creacion', 'fecha_actualizacion')

    list_display = ['id', 'titulo', 'contenido', 'imagen']
    search_fields = ['id', 'titulo', 'contenido', 'imagen']

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
admin.site.register(Preguntas, AdminPreguntas)
admin.site.register(Foro, AdminForo)
admin.site.register(ForoComentarios, AdminForoRespuesta)
admin.site.register(Capitulos, AdminCapitulo)
admin.site.register(SubCapitulos, AdminSubcapitulo)