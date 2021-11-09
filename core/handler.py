import operator
import time
import json

import akshare as ak
from django.http import HttpResponse, JsonResponse
from pandas import DataFrame


def core_handle(request):
    post = request.POST.dict()
    valuse = post.values()
    keys = post.keys()
    print(time.strftime("%H:%M:%S", time.localtime())+"-路径[%s]"%(request.path)+"-参数[%s]"%(post))
    print(post)
    if request.method == 'POST':
        api_func = getattr(ak, request.path_info.replace('/api/', ''))
        print(api_func.__name__)
        result = api_func(**post)
        print(result)
        # return HttpResponse(content=DataFrame.to_json(result, orient='records'), content_type='application/json')

    elif request.method == 'GET':
        return HttpResponse(JsonResponse({'state': False, 'reason': 'request is invalid'}))
