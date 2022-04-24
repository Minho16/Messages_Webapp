# Generated by Django 4.0.4 on 2022-04-22 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messages_webpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-time',)},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user_id',
            new_name='userid',
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
