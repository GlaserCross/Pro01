# usuario/models.py

#para tener los tipos de usuario
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_vendedor = models.BooleanField(default=False)
    is_repartidor = models.BooleanField(default=False)
    is_comprador = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'