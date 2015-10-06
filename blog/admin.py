from django.contrib import admin
from blog.models import Post


def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)
make_visible.short_description = 'Make Visible'


def make_hidden(modeladmin, request, queryset):
    queryset.update(visible=False)
make_hidden.short_description = 'Make Hidden'


class PostVisibleFilter(admin.SimpleListFilter):
    title = 'Visibility'
    parameter_name = 'visible'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Yes':
            return queryset.filter(visible=True)
        if self.value() == 'No':
            return queryset.filter(visible=False)


class PostAdmin(admin.ModelAdmin):
    change_form_template = 'admin/post_form.html'
    list_display = ['id', 'title', 'get_date', 'author', 'short_preview', 'visible']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_filter = [PostVisibleFilter]
    actions = [make_visible, make_hidden]
    list_per_page = 25


admin.site.register(Post, PostAdmin)
