from django.contrib import admin
from django.urls import path ,include
from django.http import HttpResponse
from app.views import home
import app



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("app.urls"))
]
