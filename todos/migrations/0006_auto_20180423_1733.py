# Generated by Django 2.0.3 on 2018-04-23 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_auto_20180423_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='house.Room'),
        ),
    ]
