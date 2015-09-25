from django.contrib import admin
import core.models as coremodels
# Register your models here.

admin.site.register(coremodels.Artist)
admin.site.register(coremodels.Review)