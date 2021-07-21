# Generated by Django 3.2.5 on 2021-07-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_event_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawevent',
            name='errors',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='rawevent',
            name='status',
            field=models.IntegerField(choices=[(0, 'Received'), (1, 'Processed'), (2, 'Invalid')], db_index=True, default=0),
        ),
    ]