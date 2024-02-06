# Generated by Django 5.0.1 on 2024-02-06 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_answer_alter_article_options_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='api.answer'),
        ),
        migrations.AddField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(to='api.question'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 13, 37, 57, 557704)),
        ),
        migrations.AlterField(
            model_name='test',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 13, 37, 57, 558704)),
        ),
    ]