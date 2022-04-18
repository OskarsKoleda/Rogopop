from django.contrib import admin
from .models import Event, Band


class CustomEvent(admin.ModelAdmin):
    model = Event
    list_display = ['title', 'city', 'ticket_price', 'date']
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    # list_filter = ["title", "city"]

    search_fields = ["title", "city"]


class CustomBand(admin.ModelAdmin):
    model = Band
    list_display = ['name', 'get_events']

    def get_events(self, obj):
        return "\n".join([p.title for p in obj.events_performed.all()])


admin.site.register(Event, CustomEvent)
admin.site.register(Band, CustomBand)
