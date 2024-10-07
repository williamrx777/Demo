from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<uuid:codigo>/', views.delete_filme, name='delete_filme'),
    path('update/<uuid:codigo>/', views.update_filme, name='update_filme'),
]