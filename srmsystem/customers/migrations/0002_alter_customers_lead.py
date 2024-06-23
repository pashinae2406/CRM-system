# Generated by Django 5.0.6 on 2024-06-20 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('leads', '0005_remove_leads_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='lead',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.leads'),
        ),
    ]
