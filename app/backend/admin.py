from django.contrib import admin
from .models import OCRResult
# Register your models here.
class OCRResultAdmin(admin.ModelAdmin):
    list_display = ('identification_number', 'name', 'last_name', 'date_of_birth', 'date_of_issue', 'date_of_expiry', 'created_at')

admin.site.register(OCRResult, OCRResultAdmin)