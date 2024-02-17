from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import BlackBusiness

@admin.register(BlackBusiness)
class BlackBusinessAdmin(ImportExportModelAdmin):
    search_fields = ('title',)
