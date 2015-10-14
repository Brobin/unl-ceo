from django.shortcuts import render
from schedule.models import Event


def calendar(request):
    events = Event.objects.all().order_by('start')
    return render(request, 'calendar.html', {'events': events})
