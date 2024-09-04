from django.contrib import admin
from .models import Contact

# Register your model with the admin site

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('yourname', 'email', 'subject', 'message')

