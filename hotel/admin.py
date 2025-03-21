from django.contrib import admin
from.models import *
# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ['title']

    # # Add filters for specific fields
    list_filter = ['title','price']

    # # Enable search functionality for specific fields
    search_fields = ['title'] 

    
    # # Add pagination
    list_per_page = 10

    # # # Customize ordering
    ordering = ('-created_at',)

admin.site.register(Hotel,HotelAdmin)