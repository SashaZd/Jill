# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jill_server', '0005_auto_20150403_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccquestion',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='ccreferencepapers',
            name='answer_id',
        ),
        migrations.AddField(
            model_name='ccreferencepapers',
            name='question_id',
            field=models.ForeignKey(related_name='question_id', default=1, to='jill_server.CCQuestion'),
            preserve_default=False,
        ),
    ]
