from django.contrib import admin
from .models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)

#titulo del panel
admin.site.site_header = "Master en Python - Carlos Jaramillo"
admin.site.site_title = "Master en Python - Carlos Jaramillo"
admin.site.index_title = "Panel de gestión"