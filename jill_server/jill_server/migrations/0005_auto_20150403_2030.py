# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jill_server', '0004_auto_20150403_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccprojects',
            name='document_body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ccreferencepapers',
            name='referenced_by_project',
            field=models.ManyToManyField(to='jill_server.CCProjects'),
            preserve_default=True,
        ),
    ]
