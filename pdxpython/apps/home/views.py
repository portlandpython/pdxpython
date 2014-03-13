import datetime
import json

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

import requests


def index(request):
    return render(request, 'index.html')


def meetup_calendar(request):
    request_params = {
        'key': settings.MEETUP_API_KEY,
        'group_urlname': settings.MEETUP_GROUP_NAME,
    }
    r = requests.get('http://api.meetup.com/2/events', params=request_params)
    result = r.json().get('results')
    return HttpResponse(json.dumps(result), content_type="application/json")
