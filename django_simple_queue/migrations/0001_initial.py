# Generated by Django 3.1.7 on 2021-04-08 20:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('task', models.CharField(help_text='Name of the function to be called.', max_length=127, verbose_name='Task')),
                ('args', models.TextField(blank=True, help_text='Arguments in JSON format', null=True, verbose_name='Arguments')),
                ('status', models.IntegerField(choices=[(0, 'Queued'), (1, 'In progress'), (2, 'Completed'), (3, 'Failed'), (4, 'Cancelled')], default=0, verbose_name='Status')),
                ('output', models.TextField(blank=True, null=True, verbose_name='Output')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
