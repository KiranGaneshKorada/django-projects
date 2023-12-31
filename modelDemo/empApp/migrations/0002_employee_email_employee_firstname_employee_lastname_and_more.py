# Generated by Django 4.2.2 on 2023-06-10 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='firstName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='lastName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.FloatField(null=True),
        ),
    ]
