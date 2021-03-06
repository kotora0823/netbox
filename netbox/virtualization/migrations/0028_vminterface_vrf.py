# Generated by Django 3.2.12 on 2022-02-07 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0056_standardize_id_fields'),
        ('virtualization', '0027_standardize_id_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='vminterface',
            name='vrf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vminterfaces', to='ipam.vrf'),
        ),
    ]
