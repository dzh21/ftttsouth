# -*- coding: utf-8 -*-
from django.conf import settings


def AddSettingsToContext(request):
    settings_context = {}
    for name in dir(settings):
        settings_context[name] = getattr(settings, name)
    return {'settings': settings_context}