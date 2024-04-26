# Generated by Django 5.0.4 on 2024-04-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('manager', models.BooleanField(default=False)),
            ],
        ),
    ]