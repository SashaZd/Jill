# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jill_server', '0002_ccquestion_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccquestion',
            name='question_id',
        ),
        migrations.AddField(
            model_name='ccreferencepapers',
            name='paper_author',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
