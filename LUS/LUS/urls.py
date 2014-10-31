# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from administracion.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# Login
urlpatterns += patterns('modulo.vistas.login',
url(r'^login/$', 'login_view', name="login"),
url(r'^logout/$', 'salir', name="salir"),
)

urlpatterns += patterns('modulo.vistas.inicio',
url(r'^$', 'inicio_view', name="inicio_view"),
)


# Lecciones
urlpatterns += patterns('modulo.vistas.lecciones',
url('^lecciones/$', 'lecciones_lista', name="lecciones_lista"),
url('^lecciones/(?P<id>\d+)$', 'leccion', name="leccion"),
)

# Registro
urlpatterns += patterns('modulo.vistas.registarse',
url('^registro/$', 'registrarse', name="registrarse"),
url('^activacion_cuenta/(?P<id>\d+)/(?P<clave>.+)/$', 'activar_cuenta', name="activar_cuenta"),

)

# Foro
urlpatterns += patterns('modulo.vistas.foro',
url('^foro/$', 'foro', name="foro"),
url('^foro/comentarios/(?P<id>\d+)$', 'responder_foro', name="responder_foro"),
url('^foro/comentarios/like/$', 'like_comentario', name="like_comentario"),
url('^foro/comentarios/numero_votos/$', 'get_num_votos', name="get_num_votos"),
)

# Capitulo
urlpatterns += patterns('modulo.vistas.capitulos',
url('^capitulos/$', 'capitulos', name="capitulos"),
url('^capitulos/(?P<id>\d+)$', 'leer_capitulo', name="leer_capitulo"),
url('^capitulos/prueba/$', 'capitulos_prueba', name="capitulos_prueba"),
)