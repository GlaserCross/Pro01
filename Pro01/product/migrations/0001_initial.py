# Generated by Django 3.1.2 on 2021-04-30 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Pete', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(blank=True, choices=[('F', 'Fruta'), ('V', 'Verdura'), ('H', 'Hortaliza')], default='Elija', help_text='Tipo de Producto', max_length=10)),
                ('precio', models.IntegerField()),
                ('image', models.ImageField(upload_to='static/products')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
