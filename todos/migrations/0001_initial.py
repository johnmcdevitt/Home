# Generated by Django 2.0.3 on 2018-04-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('todoid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('priority', models.CharField(choices=[('H', '3'), ('M', '2'), ('L', '1')], default='M', max_length=1)),
                ('assigned_to', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('N', 'N'), ('I', 'I'), ('C', 'C'), ('D', 'D')], default='N', max_length=1)),
            ],
        ),
    ]