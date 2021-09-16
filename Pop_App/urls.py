from django.urls import path
from . import views

urlpatterns = [
    path('', views.pop_list),
    path('pop_entry', views.pop_entry),
]

