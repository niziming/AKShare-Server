import operator
import time
import json

import akshare as ak
from django.http import HttpResponse, JsonResponse
from pandas import DataFrame


def core_handle(request):
    post = request.POST.dict()
    body = request.body.decode('utf-8')
    body = json.loads(body)
    # valuse = post.values()
    # keys = post.keys()
    print(time.strftime("%H:%M:%S", time.localtime())+"-路径[%s]"%(request.path)+"-post参数[%s]"%(post)+"-body参数[%s]"%(body))
    if request.method == 'POST':
        method = getattr(ak, request.path_info.replace('/', ''))
        return HttpResponse(content=DataFrame.to_json(method(),orient='records'), content_type='application/json')

    elif request.method == 'GET':
        return HttpResponse(JsonResponse({'state': False, 'reason': 'request is invalid'}))
