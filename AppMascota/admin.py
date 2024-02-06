from django.contrib import admin
from .models import *

# Register your models here.
# Register your models here.
admin.site.register(Avatar)
admin.site.register(Mascota)
admin.site.register(Vacuna)
admin.site.register(Consulta)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('body','created_on', 'active')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)