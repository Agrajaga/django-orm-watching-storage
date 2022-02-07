from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit, format_duration


def storage_information_view(request: HttpRequest) -> HttpResponse:
    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(visit.get_duration()),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
