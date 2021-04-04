from django.contrib import admin
from .models import Pastebin

@admin.register(Pastebin)

class PastebinAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
