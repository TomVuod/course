# Generated by Django 4.0.2 on 2022-02-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResColl', '0002_response_a_prim_response_b_prim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='part',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
