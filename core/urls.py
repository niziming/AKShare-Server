from django.urls import re_path

from core import handler

urlpatterns = [
    re_path('^', handler.core_handle)
]
