from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    change_form_template = 'admin/post_form.html'
    list_display = ['id', 'title', 'get_date', 'author', 'preview']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_per_page = 25


admin.site.register(Post, PostAdmin)
