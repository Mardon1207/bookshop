from django.contrib import admin
from .models import Customer,Contact
all_models=[Customer,Contact]
admin.site.register(all_models)
