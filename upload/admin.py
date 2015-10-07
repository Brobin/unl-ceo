from django.contrib import admin
from upload.models import Image, Document


class UploadAdmin(admin.ModelAdmin):
    exclude = ['uploaded_by']
    list_filter = ['uploaded_by__username']
    search_fields = ['title']
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not change:
            obj.uploaded_by = request.user
        obj.save()


class ImageAdmin(UploadAdmin):
    list_display = ['title', 'thumbnail', 'image', 'uploaded', 'uploaded_by']
    list_display_links = ['title', 'thumbnail', 'image']


class DocumentAdmin(UploadAdmin):
    list_display = ['title', 'document', 'uploaded', 'uploaded_by']
    list_display_links = ['title', 'document']


admin.site.register(Image, ImageAdmin)
admin.site.register(Document, DocumentAdmin)
