# Generated by Django 3.0.8 on 2020-08-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0009_agent_salt_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='salt_update_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='agent',
            name='salt_ver',
            field=models.CharField(default='1.0.3', max_length=255),
        ),
    ]