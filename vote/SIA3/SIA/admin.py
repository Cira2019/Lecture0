from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Activity)
admin.site.register(Phase)
admin.site.register(Area)
admin.site.register(Country)
admin.site.register(Status)
#admin.site.register(Intervention)
admin.site.register(Age)
admin.site.register(Extent)
admin.site.register(Target_population_source)
admin.site.register(Activity_type)
admin.site.register(YesNo)
admin.site.register(Activity_intervention)

# class Activity_typeInline(admin.TabularInline):
# 	model=Activity_type
# class InterventionAdmin(admin.ModelAdmin):
# 	inlines=[Activity_typeInline]

# admin.site.register(Intervention, InterventionAdmin)

class Activity_typeInline(admin.TabularInline):
    model = Intervention.activity_types.through
    extra=0
# class Activity_typeAdmin(admin.ModelAdmin):
#     inlines = [
#         Activity_typeInline,
#     ]

class InterventionAdmin(admin.ModelAdmin):
    inlines = [
        Activity_typeInline,
    ]

#admin.site.register(Activity_type,Activity_typeAdmin)
admin.site.register(Intervention,InterventionAdmin)
