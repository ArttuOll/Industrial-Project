from django.urls import path
from . import views

# TODO remove this example url conf
#URL conf
urlpatterns = [
    path('tiff/', views.tiff)
]