# Generated by Django 3.1.4 on 2022-05-22 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20220522_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='Username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='james', to=settings.AUTH_USER_MODEL),
        ),
    ]