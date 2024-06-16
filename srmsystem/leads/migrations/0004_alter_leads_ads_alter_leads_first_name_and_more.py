# Generated by Django 5.0.6 on 2024-06-16 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
        ('leads', '0003_alter_leads_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='ads',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.ads'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
