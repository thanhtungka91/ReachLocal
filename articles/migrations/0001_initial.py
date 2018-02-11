# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-11 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('urlToImage', models.CharField(max_length=200)),
                ('publishedAt', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Source'),
        ),
    ]
