# Generated by Django 2.0.3 on 2018-03-11 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180311_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='wallet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Portfolio'),
        ),
    ]