from django.contrib import admin

# Register your models here.
from .models import countries_all,provinces
admin.site.register(countries_all)
admin.site.register(provinces)