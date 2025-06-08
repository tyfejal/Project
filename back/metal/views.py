from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import MetalPrice  
from rest_framework.response import Response

# views.py
@api_view(['GET'])
def metal_price_chart(request, metal_type):
    # queryset = MetalPrice.objects.filter(metal_type=metal_type).order_by('date')
    queryset = MetalPrice.objects.filter(metal_type__iexact=metal_type).order_by('date')
    print(f"🔍 metal_type: {metal_type}, count: {queryset.count()}")
    data = [{'date': p.date.strftime('%Y-%m-%d'), 'price': p.price} for p in queryset]
    # return JsonResponse(data, safe=False)
    return Response(data)


