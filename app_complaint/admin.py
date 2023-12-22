from django.contrib import admin
from .models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "comment", "created_at"]  # product


admin.site.register(Complaint, ComplaintAdmin)
