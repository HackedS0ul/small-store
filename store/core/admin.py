from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    def cleanup_description(ModelAdmin, request, queryset):
        queryset.update(description="test")

    list_display = ['name', 'description','isbn_number']
    list_filter = ['name','author','in_store', 'pub_date']
    list_per_page = 3
    actions = ['cleanup_description']
    ordering = ['name']
    list_display_links = ['name']
    search_fields = ['name']