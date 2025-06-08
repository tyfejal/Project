# metal/management/commands/import_metal_prices.py

import pandas as pd
from django.core.management.base import BaseCommand
from metal.models import MetalPrice  # 모델 이름은 MetalPrice로 유지

class Command(BaseCommand):
    help = '금/은 엑셀 시세 데이터 불러오기'

    def handle(self, *args, **kwargs):
        # 1. 금 데이터 불러오기
        gold_df = pd.read_excel('Gold_prices.xlsx')  # 엑셀 경로 주의
        gold_df = gold_df.rename(columns=lambda x: x.strip())  # 혹시 모를 공백 제거

        for _, row in gold_df.iterrows():
            date = row['Date']
            price_str = str(row['Close/Last']).replace(',', '').replace('₩', '').strip()
            try:
                price = float(price_str)
            except ValueError:
                continue  # 잘못된 데이터는 건너뛴다

            MetalPrice.objects.update_or_create(
                date=date, metal_type='gold',
                defaults={'price': price}
            )

        # 2. 은 데이터 불러오기
        silver_df = pd.read_excel('Silver_prices.xlsx')  # 경로 주의
        silver_df = silver_df.rename(columns=lambda x: x.strip())  # 혹시 모를 공백 제거

        for _, row in silver_df.iterrows():
            date = row['Date']
            price_str = str(row['Close/Last']).replace(',', '').replace('₩', '').strip()
            try:
                price = float(price_str)
            except ValueError:
                continue  # 잘못된 데이터는 건너뛴다

            MetalPrice.objects.update_or_create(
                date=date, metal_type='silver',
                defaults={'price': price}
            )

        self.stdout.write(self.style.SUCCESS('✅ 금/은 시세 데이터 import 완료!'))
