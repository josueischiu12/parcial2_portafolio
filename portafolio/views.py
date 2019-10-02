from django.shortcuts import render
from django.views import generic
from .models import Proyecto, Categoria, Detalle

# Create your views here.
class ProyectoListView(generic.ListView):
    model = Proyecto
    template_name = "lista_proyectos.html"

class DetailProyecto(generic.DetailView):
    model = Proyecto
    template_name = "detalle_producto.html"

    def get_context_data(self, **kwargs):
        context = super(DetailProyecto, self).get_context_data(**kwargs)
        context["detalles"] = Detalle.objects.filter(detalle=self.object)
        return context

class CategoriaListView(generic.ListView):
    model = Categoria
    template_name = "lista_categorias.html"
