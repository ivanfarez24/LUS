# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from administracion.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('modulo.vistas.login',
url(r'^login/$', 'login_view', name="login"),
)

urlpatterns += patterns('modulo.vistas.inicio',
url(r'^$', 'inicio_view', name="inicio_view"),
)

urlpatterns += patterns('modulo.vistas.capitulo1',
url('^capitulo1/$', 'capitulo1_view', name="capitulo1_view"),
)

urlpatterns += patterns('modulo.vistas.capitulo2',
url('^capitulo2/$', 'capitulo2_view', name="capitulo2_view"),
)

# Lecciones
urlpatterns += patterns('modulo.vistas.lecciones',
url('^lecciones/(?P<id>\d+)$', 'leccion', name="leccion"),
)

# Registro
urlpatterns += patterns('modulo.vistas.registarse',
url('^registro/$', 'registrarse', name="registrarse"),
)