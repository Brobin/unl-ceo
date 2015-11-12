import datetime

from django.contrib import admin
from schedule.models import Event


class EventOverFilter(admin.SimpleListFilter):
    title = 'Time of Event'
    parameter_name = 'over'

    def lookups(self, request, model_admin):
        return (
            (None, 'All Events'),
            ('Past', 'Past Event'),
            ('Upcoming', 'Upcoming Event'),
        )

    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value() == 'Past':
            return queryset.filter(end__lt=datetime.datetime.now())
        if self.value() == 'Upcoming':
            return queryset.filter(end__gte=datetime.datetime.now())


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'preview', 'location', 'start', 'end']
    list_display_links = ['id', 'title']
    list_filter = [EventOverFilter]
    search_fields = ['title', 'location', 'description']
    list_per_page = 25


admin.site.register(Event, EventAdmin)
