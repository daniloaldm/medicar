# Generated by Django 3.0.7 on 2020-07-24 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='medico',
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ManyToManyField(to='app.Medico'),
        ),
    ]