# Generated by Django 3.1.6 on 2021-02-11 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0003_auto_20210211_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.address'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.contact'),
        ),
    ]
