from django.contrib import admin
from .views import *
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="mainview"),
    path("services/", services, name="services"),
    path("apropos/", apropos, name="apropos"),
    path("recrutement/", recrutement, name="recrutement"),
    path("contact/", contact, name="contact"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)