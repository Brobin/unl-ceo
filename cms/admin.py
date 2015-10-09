from django.contrib import admin
from cms.models import Page


class PageAdmin(admin.ModelAdmin):
    exclude = ['author']
    #change_form_template = 'admin/page_form.html'
    list_display = ['id', 'title', 'slug', 'author', 'updated']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()


admin.site.register(Page, PageAdmin)
