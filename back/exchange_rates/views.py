from datetime import datetime, timedelta
import os
import requests
import certifi
from django.http import JsonResponse
from dotenv import load_dotenv
from django.conf import settings
from django.utils.dateformat import DateFormat
from rest_framework.decorators import api_view
from rest_framework.response import Response

load_dotenv()


API_KEY = settings.EXCHANGE_API_KEY  # 환율 API 키 (.env에서 불러온 것)


@api_view(["GET"])
def today_exchange(request):
    max_retries = 7  # 최대 7일 전까지 시도
    retries = 0
    today_datetime = datetime.now()
    while retries < max_retries:
        today = DateFormat(today_datetime).format("Ymd")
        url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON/"
        params = {"authkey": API_KEY, "data": "AP01", "searchdate": today}
        response = requests.get(url, params=params, verify=False)

        print(f"[환율 요청] 날짜: {today}, 상태코드: {response.status_code}")

        if response.status_code == 200:
            response_json = response.json()
            if response_json:  # 비어 있지 않으면 데이터를 반환
                return Response(response_json)

        # 데이터를 찾지 못한 경우 하루 전으로 이동
        today_datetime -= timedelta(days=1)
        retries += 1
    # 모든 시도에서 데이터를 찾지 못한 경우
    return Response({"error": "데이터를 찾지 못 했습니다."}, status=404)

