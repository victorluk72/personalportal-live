# https://www.youtube.com/watch?v=G-Rct7Na0UQ&t=399s
import django_filters
from .models import PersonalContact, BusinessContact, BusinesType


class PContactFilter(django_filters.FilterSet):
    lastName = django_filters.CharFilter(lookup_expr='icontains', label='')

    class Meta:
        model = PersonalContact
        fields = ['lastName']


class PAdvContactFilter(django_filters.FilterSet):
    firstName = django_filters.CharFilter(lookup_expr='icontains', label='')
    lastName = django_filters.CharFilter(lookup_expr='icontains', label='')
    emailPersonal = django_filters.CharFilter(
        lookup_expr='icontains', label='')
    emailWork = django_filters.CharFilter(lookup_expr='icontains', label='')

    class Meta:
        model = PersonalContact
        fields = ['contactType', 'firstName',
                  'lastName', 'emailPersonal', 'emailWork']


class BContactFilter(django_filters.FilterSet):
    businessName = django_filters.CharFilter(lookup_expr='icontains', label='')

    class Meta:
        model = BusinessContact
        fields = ['businessName']


class BAdvContactFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(lookup_expr='icontains', label='')
    contactName = django_filters.CharFilter(lookup_expr='icontains', label='')
    note = django_filters.CharFilter(lookup_expr='icontains', label='')

    class Meta:
        model = BusinessContact
        fields = ['businessType', 'contactName', 'email', 'country', 'note']
