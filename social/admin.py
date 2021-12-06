from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
    # extiende la función readonly_fields en tiempo de ejecución
    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name='Personal').exists():
            return ['key', 'name']
        else:
            return ['created', 'updated']

admin.site.register(Link, LinkAdmin)
