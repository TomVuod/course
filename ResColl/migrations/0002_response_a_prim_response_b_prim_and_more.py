# Generated by Django 4.0.2 on 2022-02-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResColl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='a_prim',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='b_prim',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='correlation_prim',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='min_y_prim',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
    ]
