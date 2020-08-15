# Generated by Django 3.0.8 on 2020-08-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('num', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('pass1', models.CharField(max_length=30)),
            ],
        ),
    ]
