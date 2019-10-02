from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete

# Create your models here.
class Categoria(models.Model):
    """Model definition for Categoria."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre

class Proyecto(models.Model):
    """Model definition for Proyecto."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="portafolio")
    categoria_id = models.ForeignKey(Categoria, on_delete= models.PROTECT)

    class Meta:
        """Meta definition for Proyecto."""

        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        """Unicode representation of Proyecto."""
        return self.nombre

    def get_absolute_url(self):
        return u'/proyecto/%d' % self.id

class Detalle(models.Model):
    """Model definition for Detalle."""

    # TODO: Define fields here
    proyecto_id = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="portafolio")

    class Meta:
        """Meta definition for Detalle."""

        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'

    def __str__(self):
        """Unicode representation of Detalle."""
        return self.codigo

