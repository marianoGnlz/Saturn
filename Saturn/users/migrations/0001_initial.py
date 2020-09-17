# Generated by Django 3.1.1 on 2020-09-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('fechaDeNacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], max_length=1)),
            ],
        ),
    ]