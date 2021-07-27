from django.contrib import admin
from app.models import livro, emprestimo


# Register your models here.

class LivroAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "autor", "tipo")
    list_display_links = ("id", "nome", "autor", "tipo")
    list_per_page = 30

admin.site.register(livro, LivroAdmin)
admin.site.register(emprestimo)