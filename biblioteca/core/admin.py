from django.contrib import admin

# Register your models here.
from .models import Livro, Categoria, Autor


class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "publicado_em"]
    search_fields = ["titulo", "autor"]


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    search_fields = ["nome"]

class AutorAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    search_fields = ["nome"]


admin.site.register(Livro, LivroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
