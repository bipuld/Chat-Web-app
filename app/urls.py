from django.urls import path
from . import views

urlpatterns = [
    # ... your existing URL patterns ...
    path('', views.home,name="views"),
]
