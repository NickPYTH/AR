# Generated by Django 5.0.1 on 2024-02-06 08:47

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_question_test_question_answers_test_questions_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=250, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=150, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='Тело статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 13, 47, 10, 613902), verbose_name='Дата и время публикации'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.IntegerField(verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='api.answer', verbose_name='Ответы'),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='test',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='test',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='test',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 13, 47, 10, 614901), verbose_name='Дата и время публикации'),
        ),
        migrations.AlterField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(to='api.question', verbose_name='Вопросы'),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='profile',
            name='achievements',
            field=models.ManyToManyField(to='api.achievement', verbose_name='Достижения'),
        ),
    ]