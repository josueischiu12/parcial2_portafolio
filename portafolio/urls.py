from django.urls import path

from . import views

app_name = "portafolio"
urlpatterns = [
    path("proyecto/", views.ProyectoListView.as_view(), name="lista_proyectos"),
    # path("create/", views.CreateProyectoView.as_view(), name="nuevo_proyecto"),
    # path("<int:pk>/", views.DetailProyectoView.as_view(), name="detalle_proyecto"),
    # path("<int:pk>/update/", views.UpdateProyectoView.as_view(), name="editar_proyecto"),
    # path("<int:pk>/delete/", views.DeleteProyectoView.as_view(), name="eliminar_proyecto"),
    
    path("categoria/", views.CategoriaListView.as_view(), name="lista_categorias"),
]