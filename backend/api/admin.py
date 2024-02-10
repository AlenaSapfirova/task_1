from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'header', 'text', 'published',
                    'date_created']
    list_editable = ['author', 'header']


admin.site.register(Post, PostAdmin)
