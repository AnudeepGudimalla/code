from django.contrib import admin
from django.urls import path, include   #new

from .views import home_page_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),     #new
]