from django.contrib import admin
from blog.models import Post


def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)
make_visible.short_description = 'Make Visible'


def make_hidden(modeladmin, request, queryset):
    queryset.update(visible=False)
make_hidden.short_description = 'Make Hidden'


class PostAdmin(admin.ModelAdmin):
    exclude = ['author']
    change_form_template = 'admin/post_form.html'
    list_display = ['id', 'title', 'get_date', 'author', 'short_preview', 'visible']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_filter = ['visible', 'author__username']
    actions = [make_visible, make_hidden]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
