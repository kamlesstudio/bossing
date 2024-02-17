from django.db.models import Q
import django_filters

from django.forms.widgets import TextInput
from bossing_up.models import *

class BusinessFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='category_custom_filter', widget=TextInput(attrs={'placeholder':'Business'}))
    
    class Meta:
        model = BlackBusiness
        fields = ['category']


    def category_custom_filter(self, queryset, name, value):
        return BlackBusiness.objects.filter(
            Q(category__icontains=value) | Q(tags__icontains=value) | Q(keyword__icontains=value) | Q(title__icontains=value)
        )
