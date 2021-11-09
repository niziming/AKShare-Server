import operator

import akshare as ak
from django.http import HttpResponse, JsonResponse
from pandas import DataFrame


def core_handle(request):
    print(request)
    if request.method == 'POST':
        method = getattr(ak, request.path_info.replace('/api/', ''))
        return HttpResponse(content=DataFrame.to_json(method(),orient='records'), content_type='application/json')

    elif request.method == 'GET':
        return HttpResponse(JsonResponse({'state': False, 'reason': 'request is invalid'}))
