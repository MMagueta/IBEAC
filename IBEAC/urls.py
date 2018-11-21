from django.contrib import admin
from django.urls import path
from forum import urls
from django.conf.urls import include
import forum.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include("forum.urls")),
]
