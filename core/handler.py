import operator
import time
import json

import akshare as ak
from django.http import HttpResponse, JsonResponse
from pandas import DataFrame


def core_handle(request):
    # post = request.POST.dict()
    # param = {'fund': '710001', 'indicator': '累计收益率走势'}
    #
    # # body = request.body.decode('utf-8')
    # # param = post
    # if request.method == 'POST':
    #     result = getattr(ak, request.path_info.replace('/', ''))(**post)
    #     return HttpResponse(content=DataFrame.to_json(result, orient='records'), content_type='application/json')

    param = dict()
    post = request.POST.dict()
    body = request.body.decode('utf-8')
    if not post:
        if body and (not body.strip() == ''):
            param = json.loads(body)
    else:
        param = post

    print(time.strftime("%H:%M:%S", time.localtime()) + "-路径[%s]" % (request.path) + "-post参数[%s]" % (post) + "-body参数[%s]" % (body))

    if request.method == 'POST':
        if not param:
            method = getattr(ak, request.path_info.replace('/', ''))
            return HttpResponse(content=DataFrame.to_json(method(), orient='records'), content_type='application/json')
        else:
            method = getattr(ak, 'fund_em_open_fund_info')(**param)
            return HttpResponse(content=DataFrame.to_json(method, orient='records'), content_type='application/json')

    elif request.method == 'GET':
        return HttpResponse(JsonResponse({'state': False, 'reason': 'request is invalid'}))
