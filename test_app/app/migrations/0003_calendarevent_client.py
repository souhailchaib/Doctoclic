# Generated by Django 4.2.9 on 2024-04-29 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_calendarevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.clientmodel'),
            preserve_default=False,
        ),
    ]
