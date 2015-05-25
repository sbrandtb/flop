from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from flop.payment.fields import CurrencyField


class MealContribution(models.Model):
    meal = models.ForeignKey(
        'Meal',
        verbose_name=_('meal'))
    contributor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('contributor'))
    amount = CurrencyField(
        _('amount'),
        validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = _('meal contribution')
        verbose_name_plural = _('meal contributions')

    def __unicode__(self):
        return _('%(amount)s for %(meal)s by %(contributor_name)s') % {
            'amount': self.amount,
            'meal': self.meal,
            'contributor_name': self.contributor,
        }


class Meal(models.Model):
    eaten_on = models.DateTimeField(
        _('eaten on'),
        auto_now_add=True)
    chef = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='cooked',
        verbose_name=_('chef'))
    description = models.CharField(
        _('description'),
        max_length=64)
    guests = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='ate_from',
        verbose_name=_('guests'))
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through=MealContribution,
        related_name='contributed_to',
        verbose_name=_('contributors'))

    class Meta:
        verbose_name = _('meal')
        verbose_name_plural = _('meals')

    def __unicode__(self):
        return _('%(description)s by %(chef)s on %(date)s') % {
            'name': self.description,
            'chef': self.chef,
            'date': self.eaten_on,
        }
