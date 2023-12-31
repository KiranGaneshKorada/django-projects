# Generated by Django 4.2.2 on 2023-06-25 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientsApp', '0002_rename_patientdata_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientClinicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('bloodPressure', models.IntegerField()),
                ('heartRate', models.IntegerField()),
                ('Patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patientsApp.patient')),
            ],
        ),
    ]
