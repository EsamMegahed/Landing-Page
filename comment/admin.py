from django.contrib import admin
from . models import *
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ['name']

    # # Add filters for specific fields
    list_filter = ['country','date','stars']

    # # Enable search functionality for specific fields
    search_fields = ['name'] 

    
    # # Add pagination
    list_per_page = 15

    # # # Customize ordering
    ordering = ('-created_at',)
    
admin.site.register(Comment,CommentAdmin)