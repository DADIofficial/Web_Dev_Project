# Generated by Django 5.0.4 on 2024-04-23 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0004_alter_tikets_acc_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tikets',
            name='Acc_id',
        ),
        migrations.RemoveField(
            model_name='tikets',
            name='Sec_tic',
        ),
        migrations.CreateModel(
            name='Buy_Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Per_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviato.account')),
                ('Tikets_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviato.tikets')),
            ],
        ),
    ]
