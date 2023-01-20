from django.contrib import admin
from clothes.models import Category, Institution, Donation


admin.site.register(Category)
# admin.site.register(Institution)
admin.site.register(Donation)


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "type"]

