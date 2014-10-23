#! /usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'Ivan'

from django.conf import settings


def global_vars(request):
    """
     variables globales de templates
    :return:
    """
    return {'URL_ROOT': settings.URL}