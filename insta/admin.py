from django.contrib import admin
from django.apps import apps
# Register your models here.


all_models = apps.get_models()

for model in all_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

