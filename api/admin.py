from django.contrib import admin
from .models import Customer,Contact,Publisher,Language,Book,Author,Genre
all_models=[Customer,Contact,Publisher,Language,Book,Author,Genre]
admin.site.register(all_models)
