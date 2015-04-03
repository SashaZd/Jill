# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jill_server', '0003_auto_20150331_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccquestion',
            name='asked_by_user',
        ),
        migrations.RemoveField(
            model_name='ccquestion',
            name='evidence_list',
        ),
    ]
