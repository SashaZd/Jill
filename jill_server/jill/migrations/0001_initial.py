# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(max_length=200)),
                ('confidence', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('answers', models.ForeignKey(to='jill.Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferencePapers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evidence_text', models.CharField(max_length=200)),
                ('paper_title', models.CharField(max_length=200)),
                ('paper_link', models.CharField(max_length=200)),
                ('answer_id', models.ForeignKey(related_name='answer_id', to='jill.Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='asked_by_user',
            field=models.ForeignKey(related_name='asked_by_user', to='jill.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='evidence_list',
            field=models.ForeignKey(to='jill.ReferencePapers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='from_project_id',
            field=models.ForeignKey(related_name='from_project_id', to='jill.Projects'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projects',
            name='created_by_user',
            field=models.ForeignKey(related_name='created_by_user', to='jill.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='evidence_list',
            field=models.ForeignKey(to='jill.ReferencePapers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(to='jill.Question'),
            preserve_default=True,
        ),
    ]
