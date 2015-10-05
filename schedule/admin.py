import datetime

from django.contrib import admin
from schedule.models import Event


class EventOverFilter(admin.SimpleListFilter):
    title = 'event over'
    parameter_name = 'over'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Yes':
            return queryset.filter(end__lt=datetime.datetime.now())
        if self.value() == 'No':
            return queryset.filter(end__gte=datetime.datetime.now())


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'location', 'start', 'end']
    list_display_links = ['id', 'title']
    list_filter = [EventOverFilter]
    search_fields = ['title', 'location', 'description']
    list_per_page = 25


admin.site.register(Event, EventAdmin)
