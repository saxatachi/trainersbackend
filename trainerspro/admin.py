from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(TrainerHoursPerDay)
admin.site.register(Event)
admin.site.register(Package)
