from django.shortcuts import render
from schedule.models import Event
import datetime


def calendar(request):
    now = datetime.datetime.now()
    events = Event.objects.filter(end__gte=now).order_by('start')
    return render(request, 'calendar.html', {'events': events})
