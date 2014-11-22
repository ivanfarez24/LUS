#! /usr/bin/python
# -*- coding: UTF-8-*-
__author__ = 'Ivancho'

from django import forms


class Foroform(forms.Form):
    tema = forms.CharField(widget=forms.Textarea, label="Tema")
    pregunta = forms.CharField(widget=forms.Textarea, label="Pregunta")

    def get_tema(self):
        return self.cleaned_data["tema"]

    def get_pregunta(self):
        return self.cleaned_data["pregunta"]

    def __init__(self, *args, **kwargs):
        super(Foroform, self).__init__(*args, **kwargs)
        self.fields['tema'].widget.attrs['rows'] = "3"
        self.fields['tema'].widget.attrs['placeholder'] = "Tema"
        self.fields['pregunta'].widget.attrs['placeholder'] = "Pregunta"
        self.fields['pregunta'].widget.attrs['rows'] = "3"

