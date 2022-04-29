# Generated by Django 4.0.4 on 2022-04-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('nick_name', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
