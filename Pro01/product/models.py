from django.db import models
from django.utils.text import slugify
from usuario.models import User
from django.urls import reverse

import uuid
# Create your models here.


class product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    TIPO_PRODUC = (
        ('Fruta', 'Fruta'),
        ('Fruta','Verdura'),
        ('Fruta','Hortaliza')
        )

    tipo = models.CharField(
        max_length = 10,
        choices=TIPO_PRODUC,
        blank=True,
        default='Elija',
        help_text = 'Tipo de Producto'
        )

    precio = models.IntegerField()

    image = models.ImageField(
        upload_to='media',blank=True,
        default = 'products/noimage.png') 

    class Meta:
        pass
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.nombre},{self.tipo},{self.precio},{self.image}'