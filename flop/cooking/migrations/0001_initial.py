# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flop.payment.fields
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eaten_on', models.DateTimeField(auto_now_add=True, verbose_name='eaten on')),
                ('description', models.CharField(max_length=64, verbose_name='description')),
                ('chef', models.ForeignKey(related_name='cooked', verbose_name='chef', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'meal',
                'verbose_name_plural': 'meals',
            },
        ),
        migrations.CreateModel(
            name='MealContribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', flop.payment.fields.CurrencyField(verbose_name='amount', max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('contributor', models.ForeignKey(verbose_name='contributor', to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(verbose_name='meal', to='cooking.Meal')),
            ],
            options={
                'verbose_name': 'meal contribution',
                'verbose_name_plural': 'meal contributions',
            },
        ),
        migrations.AddField(
            model_name='meal',
            name='contributors',
            field=models.ManyToManyField(related_name='contributed_to', verbose_name='contributors', through='cooking.MealContribution', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meal',
            name='guests',
            field=models.ManyToManyField(related_name='ate_from', verbose_name='guests', to=settings.AUTH_USER_MODEL),
        ),
    ]
