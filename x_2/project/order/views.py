from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.conf import settings
import pandas as pd
import os

def getOrder(request):
    """
    R ( int recency )
    F ( int frequency )
    M ( int monetary )
    ID (int ID)

    將 ID 以倒 R 值排序回傳 (大到小) ( function sort_by_recency( ) )
    將 ID 以倒 F 值排序回傳 (大到小) ( function sort_by_frequency( ) )
    將 ID 以 M 值排序回傳 (小到大) ( function sort_by_monetary( ) )
    將 ID 以倒 RFM 總值排序回傳 (大到小) ( function sort_by_RFM( ) )

    rtype : json
    """

    method = request.GET.get('method','R')
    file_dir = os.path.join(settings.STATICFILES_DIRS[0], 'rfm.csv')
    
    data = pd.read_csv(file_dir)

    if method == 'R':
        result = data.sort_values('R', ascending = False)['ID'].values
        return JsonResponse(result.tolist(), safe=False)
    if method == 'F':
        result = data.sort_values('F', ascending = False)['ID'].values
        return JsonResponse(result.tolist(), safe=False)
    if method == 'M':
        result = data.sort_values('M', ascending = True)['ID'].values
        return JsonResponse(result.tolist(), safe=False)
    if method == 'RFM':
        data.loc[:, "RFM"] = data["R"] + data["F"] + data["M"]
        RFM = data.sort_values('RFM', ascending = False)['ID'].values
        return JsonResponse(RFM.tolist(), safe=False)
