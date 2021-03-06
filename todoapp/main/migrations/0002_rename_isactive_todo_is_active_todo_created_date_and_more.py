# Generated by Django 4.0.5 on 2022-06-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
