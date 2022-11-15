from django.urls import path
from .views import *

app_name = 'portfolio'

urlpatterns = [
    path("", index_view, name="home"),
]