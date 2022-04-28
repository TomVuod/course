# Generated by Django 4.0.2 on 2022-02-23 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean_x', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('mean_y', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('sd_y', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('correlation', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('condition_counter', models.PositiveIntegerField(blank=True, null=True)),
                ('a', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('b', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('max_dev_x', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('tss', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True)),
                ('residual_sd', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('mean_residual', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('timestamp', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
