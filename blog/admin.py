from django.contrib import admin

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    # selecciona las columnas a mostrar en el detalle
    list_display = ['title', 'author', 'published', 'post_categories']
    ordering = ['author', 'published']
    # formulario de búsqueda
    search_fields = ['title', 'content', 'author__username', 'categories__name']
    # organiza por jerarquía de fechas
    date_hierarchy = 'published'
    # listado de filtros
    list_filter = ['author__username', 'categories__name']

    # método para mostrar en el detalle las categorías
    def post_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all().order_by('name'))
    # reescribe el nombre de la columna
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
