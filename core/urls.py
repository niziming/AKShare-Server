from django.urls import re_path

from core import handler

urlpatterns = [
    re_path('^api/', handler.core_handle)
]
