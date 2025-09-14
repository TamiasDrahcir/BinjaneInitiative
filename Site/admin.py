from django.contrib import admin
from .models import profile, gallery, category


admin.site.register(gallery)
admin.site.register(profile)
admin.site.register(category)

# Register your models here.
