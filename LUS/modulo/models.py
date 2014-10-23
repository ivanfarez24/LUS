#! /usr/bin/python
# -*- coding: UTF-8 -*-

from django.db import models
import datetime
from django.contrib.auth.admin import User

# Create your models here.


class ModuloTexto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, unique=True)
    titulo = models.CharField(max_length=200, null=True, blank=True)
    imagen = models.CharField(max_length=200, null=True, blank=True)
    texto = models.TextField()

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_actualizacion = models.CharField(max_length=60)

    class Meta():
        db_table = "modulo_texto"
        verbose_name = "Modulo Texto"
        verbose_name_plural = "Modulos Texto"


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=220)
    imagen = models.CharField(max_length=220, null=True, blank=True)
    url = models.CharField(max_length=220, null=True, blank=True)
    name_url = models.CharField(max_length=220, null=True, blank=True)
    orden = models.IntegerField(default=0)
    grupo_menu = models.ForeignKey('self', blank=True, null=True, db_column="grupo_menu_id")  # Relación a si misma


    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "menu"
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def get_submenus(self):
        """
        Retorna todos los submenus activos
        :return:
        """
        return Menu.objects.filter(grupo_menu=self, estado=True)


class Sexo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=220)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "sexo"
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"


class Estado_civil(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=220)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "estado_civil"
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estados Civiles"


class Permiso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=220)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    app = models.ForeignKey(Menu)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "permiso"
        verbose_name = "Permiso"
        verbose_name_plural = "Permisos"


class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=220)
    permisos = models.ManyToManyField(Permiso)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "grupo"
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"


class Persona(User):
    grupo = models.ManyToManyField(Grupo, blank=True)
    permisos = models.ManyToManyField(Permiso, null=True, blank=True)
    cedula = models.CharField(max_length=20, null=True, unique=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    sexo = models.ForeignKey(Sexo)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    estado_civil = models.ForeignKey(Estado_civil, null=True, blank=True)
    clave_temp = models.CharField(max_length=220, null=True, blank=True)
    referencia = models.CharField(max_length=220, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)

    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "persona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class Leccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=220)

    numero = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    col_rep2 = models.CharField(max_length=250, null=True, blank=True)

    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "leccion"
        verbose_name = "Lección"
        verbose_name_plural = "Lecciones"

    def get_preguntas(self):
        """
        Obtiene las preguntas de cada lección
        :return:
        """
        return Preguntas.objects.filter(leccion=self).order_by('numero')


class Preguntas(models.Model):
    id = models.AutoField(primary_key=True)
    leccion = models.ForeignKey(Leccion)
    descripcion = models.TextField()

    numero = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    col_rep2 = models.CharField(max_length=250, null=True, blank=True)

    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "preguntas"
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def get_respuestas(self):
        """
        Obtiene las respuestas de cada pregunta
        :return:
        """
        return Respuestas.objects.filter(preguntas=self).order_by('numero')


class Respuestas(models.Model):
    """
     La clase respuesta tiene la puntuación de cada pregunta, si la puntuación es cero
     es una respuesta incoreecta
    """
    id = models.AutoField(primary_key=True)
    preguntas = models.ForeignKey(Preguntas)
    nombre = models.CharField(max_length=220)
    puntuacion = models.FloatField(default=0)
    numero = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    col_rep2 = models.CharField(max_length=250, null=True, blank=True)

    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "respuestas"
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"


class Foro(models.Model):
    def url(self, filename):
        ruta = str("foro/%s" % filename)
        return ruta

    id = models.AutoField(primary_key=True)
    tema = models.TextField()
    pregunta = models.TextField()
    numero_visitas = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to=url, null=True, blank=True)
    persona = models.ForeignKey(Persona)
    estado = models.BooleanField(default=True)
    col2 = models.CharField(max_length=550, null=True, blank=True)
    
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "foro"
        verbose_name = "Foro"
        verbose_name_plural = "Foros"

    def get_respuestas(self):
        """
            retorna la lista de todas las respuestas
            del foro que están activas
        """
        return ForoComentarios.objects.filter(foro=self)

    def get_num_resp(self):
        """
            retorna el número de todas las respuestas
            del foro que están activas
        """
        return len(ForoComentarios.objects.filter(foro=self))


class ForoComentarios(models.Model):
    def url(self, filename):
        ruta = str("foro/%s" % filename)
        return ruta

    id = models.AutoField(primary_key=True)
    foro = models.ForeignKey(Foro)
    persona = models.ForeignKey(Persona)

    comentario = models.TextField()
    numero_votos = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to=url, null=True, blank=True)

    estado = models.BooleanField(default=True)
    col2 = models.CharField(max_length=550, null=True, blank=True)

    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "foro_comentario"
        verbose_name = "Foro Comentario"
        verbose_name_plural = "Comentarios de Foros"


class PersonaVotoComentario(models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona)
    foro_comentario = models.ForeignKey(ForoComentarios)

    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "persona_voto_comentario"
        verbose_name = "Persona voto comentario"
        verbose_name_plural = "Persona voto comentarios"

class Capitulos(models.Model):
    def url(self, filename):
        ruta = str("foro/%s" % filename)
        return ruta

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=550, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    imagen = models.ImageField(upload_to=url, null=True, blank=True)

    # Columnas aprovisionadas
    orden = models.IntegerField(default=0)
    col2 = models.CharField(max_length=550, null=True, blank=True)

    estado = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "capitulo"
        verbose_name = "Capitulo"
        verbose_name_plural = "Capitulos"

    def get_subcapitulos(self):
        return SubCapitulos.objects.filter(capitulo=self, estado=True).order_by("orden")


class SubCapitulos(models.Model):
    def url(self, filename):
        ruta = str("foro/%s" % filename)
        return ruta

    id = models.AutoField(primary_key=True)
    capitulo = models.ForeignKey(Capitulos)
    titulo = models.CharField(max_length=550, null=True, blank=True)
    contenido = models.TextField(null=True, blank=True)

    imagen = models.ImageField(upload_to=url, null=True, blank=True)

    # Columnas aprovisionadas
    orden = models.IntegerField(default=0)
    animacion = models.TextField(null=True, blank=True)

    estado = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(default=datetime.datetime.now().date())
    usuario_creacion = models.CharField(max_length=60)
    fecha_actualizacion = models.DateTimeField(default=datetime.datetime.now().date(), null=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "subcapitulo"
        verbose_name = "Subcapitulo"
        verbose_name_plural = "Subcapitulos"