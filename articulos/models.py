from django.db import models
#los modelos se crean mediante clases 
# Create your models here.
class Entrada(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=400)
    imagen = models.URLField(max_length=300)
    autor = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre