# Generated by Django 5.0.1 on 2024-02-06 08:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Обучающая статья', 'verbose_name_plural': 'Обучающие статьи'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили пользователей'},
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 13, 31, 12, 582647)),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2024, 2, 6, 13, 31, 12, 582647))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
            options={
                'verbose_name': 'Проверочный тест',
                'verbose_name_plural': 'Проверочные тесты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.test')),
            ],
            options={
                'verbose_name': 'Вопрос для теста',
                'verbose_name_plural': 'Вопросы для тестов',
            },
        ),
    ]
