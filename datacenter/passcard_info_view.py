from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit, format_duration


def passcard_info_view(request: HttpRequest, passcode: str) -> HttpResponse:
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard):
        this_passcard_visits.append(
            {
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(visit.get_duration()),
                'is_strange': visit.is_long()
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
