from django.contrib import admin
from .models import PrivacyPolicy, Review


def duplicate(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate.short_description = "Copy select element"

class AdminProject(admin.ModelAdmin):
    actions = [duplicate]

admin.site.register(PrivacyPolicy)
admin.site.register(Review, AdminProject)