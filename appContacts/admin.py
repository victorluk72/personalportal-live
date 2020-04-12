from django.contrib import admin
from .models import PersonalContact, ChildContact,BusinesType,BusinessContact

# Register your models here.
admin.site.register(PersonalContact)
admin.site.register(ChildContact)
admin.site.register(BusinesType)
admin.site.register(BusinessContact)
