from django.contrib import admin

from . import models
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Now the Notes model is attach to the NotesAdmin model
admin.site.register(models.Notes, NotesAdmin)