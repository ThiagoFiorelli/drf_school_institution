# Generated by Django 3.1.6 on 2021-02-11 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0004_auto_20210211_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institution.address'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institution.contact'),
        ),
    ]
