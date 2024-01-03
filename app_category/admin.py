from django.contrib import admin
from .models import Category, PodCategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'img']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(PodCategory)
class PodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'img']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
