from django.urls import path
from . import views

urlpatterns = [
    # ... your existing URL patterns ...
    path('<str:groupname>/', views.home,name="views"),
    
]
