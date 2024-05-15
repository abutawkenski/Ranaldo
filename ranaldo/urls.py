from django.urls import path
from .views import ranaldo

urlpatterns = [
    path("", ranaldo, name="ranaldo")
]