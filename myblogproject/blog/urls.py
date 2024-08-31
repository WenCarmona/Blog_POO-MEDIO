from django.urls import path
from .import views

urlpatterns = [
    path('',views.lista_publicaciones, name='lista_publicaciones'),
    path('post/<int:pk/', views.detalle_publicacion, name='detalle_publicacion'),
]