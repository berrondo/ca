# Generated by Django 3.2.5 on 2021-07-20 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rawevent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['session_id', 'timestamp']},
        ),
    ]