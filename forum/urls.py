from django.urls import path
from django.conf.urls import include
from . import views as forum_views

urlpatterns = [
    path('', forum_views.home, name="Home")
]
