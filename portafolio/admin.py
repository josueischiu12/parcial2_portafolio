from django.contrib import admin
from .models import Categoria, Proyecto, Detalle

# Register your models here.
admin.site.register(Categoria)

class DetalleInLine(admin.TabularInline):
    model = Detalle
    extra = 1

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "fecha", "imagen", "categoria_id",)

    inlines = [
        DetalleInLine,
    ]