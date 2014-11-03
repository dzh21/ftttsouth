# -*- coding: utf-8 -*-
from django.conf import settings


def AddSettingsToContext(request):
    return {'settings': settings}