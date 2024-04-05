from django.contrib import admin
from django.urls import path,include
import Front.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Front.urls")),
    path("request/", include("Back.urls")),
]
