# Generated by Django 3.0.3 on 2020-07-20 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20200720_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_last_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
