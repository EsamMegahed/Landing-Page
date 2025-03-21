from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from.models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ['name']

    # # Add filters for specific fields
    list_filter = ['name','subject']

    # # Enable search functionality for specific fields
    search_fields = ['name'] 

    # Make fields read-only
    readonly_fields = ['name','email','phone','subject','message']
    # # Add pagination
    list_per_page = 20

    # # Customize ordering
    ordering = ('-created_at',)
 
admin.site.register(Contact,ContactAdmin)