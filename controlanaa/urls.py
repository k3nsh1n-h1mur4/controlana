from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listado/', views.list, name='list'),
    path('registro_nuevo/', views.register_new, name='register_new'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.elimiar_registro, name='eliminar'),
]
