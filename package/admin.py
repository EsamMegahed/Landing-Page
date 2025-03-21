from django.contrib import admin
from.models import *

# Register your models here.
admin.site.site_header = "El_Tawasul"
admin.site.site_title = "My Custom Admin Portal"
admin.site.index_title = "El_Tawasul"


class PackageAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ['title']
    
    # # Add filters for specific fields
    list_filter = ['title','start_date']

    # # Enable search functionality for specific fields
    search_fields = ['title'] 

    
    # # Add pagination
    list_per_page = 15

    # # # Customize ordering
    ordering = ('-created_at',)

admin.site.register(Hajj,PackageAdmin)
admin.site.register(Umrah,PackageAdmin)