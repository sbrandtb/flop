from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from flop.cooking.forms import MealForm, MealContributionFormSet
from flop.decorators import view_decorator


@view_decorator(login_required)
class IndexView(TemplateView):
    template_name = 'dashboard/index.html'
