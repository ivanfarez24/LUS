# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from administracion.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('modulo.vistas.login',
url('^/$', 'login', name="login"),
)

urlpatterns += patterns('modulo.vistas.inicio',
url('^inicio2/$', 'inicio_view', name="inicio_view2"),
)

urlpatterns += patterns('modulo.vistas.inicio2',
url('^inicio/$', 'inicio_view', name="inicio_view"),
)

urlpatterns += patterns('modulo.vistas.capitulo1',
url('^capitulo1/$', 'capitulo1_view', name="capitulo1_view"),
)

urlpatterns += patterns('modulo.vistas.capitulo2',
url('^capitulo2/$', 'capitulo2_view', name="capitulo2_view"),
)