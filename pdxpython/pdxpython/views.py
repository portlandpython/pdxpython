import datetime

from django.conf import settings
from django.shortcuts import render

import requests


def index(request):
    print settings.MEETUP_API_KEY
    request_params = {
        'key': settings.MEETUP_API_KEY,
        'group_urlname': settings.MEETUP_GROUP_NAME,
    }
    r = requests.get('http://api.meetup.com/2/events', params=request_params)
    results = r.json().get('results')
    for result in results:
        result['date'] = datetime.datetime.utcfromtimestamp(result['time'] / 1000)
    return render(request, 'pdxpython/index.html', {'events': results})
