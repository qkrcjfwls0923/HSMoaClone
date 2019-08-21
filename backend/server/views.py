from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.utils.timezone import utc
from tqdm import tqdm
from sklearn.externals import joblib

from .models import ShoppingMall, Category, Item

# Create your views here.
class SetupView(View):
    def get(self, request):
        datas = joblib.load("timeline_goods_dump.dat")
        if len(datas) is not 0:
            for data in tqdm(datas):
                self.parse_data(data)

        return JsonResponse({
            "success": True
        })

    def parse_data(self, data):
        mall_name = {
            "cjmall": "cj쇼핑몰",
            "gsshop": "gs쇼핑몰",
            "lottemall": "롯데몰",
            "hmall": "현대홈쇼핑"
        }

        mall = ShoppingMall.objects.filter(name=data["genre2"]).first()
        if mall is None:
            mall = ShoppingMall(name=data["genre2"], label=mall_name[data["genre2"]])
            mall.save()
        
        cate_name=data["cate1"]
        if cate_name is None:
            cate_name=""
        
        cate = Category.objects.filter(name=cate_name).first()
        if cate is None:
            cate = Category(name=data["cate1"])
            cate.save()

        date = datetime.strptime(str(data["date"]), "%Y%m%d")
        start_time=str(data["start_time"])
        offset=len(start_time)-2
        hour=int(start_time[:offset]) if start_time[:offset] else 0
        minute=int(start_time[offset:]) if start_time[offset:] else 0
        start_time=datetime(year=date.year, month=date.month, day=date.day, hour=hour, minute=minute)

        end_time=str(data["end_time"])
        offset=len(end_time)-2
        hour=int(end_time[:offset]) if end_time[:offset] else 0
        minute=int(end_time[offset:]) if end_time[offset:] else 0
        end_time=datetime(year=date.year, month=date.month, day=date.day, hour=hour, minute=minute)

        item=Item(name=data["name"], mall=mall, start_time=start_time, 
            end_time=end_time, category=cate, url=data["url"], img=data["img"], price=data["price"],
            org_price=data["org_price"])
        item.save()