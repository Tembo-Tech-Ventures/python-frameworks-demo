from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'content')
    search_fields = ('title', 'content')

admin.site.register(Note, NoteAdmin)