import json
from datetime import datetime, timedelta

from django.db.models import Q
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

class ItemView(View):
    def get(self, request, date, time, mall, category, orderby):
        dt=datetime.strptime(date, "%Y%m%d")
        offset=len(time)-2
        hour=int(time[:offset]) if time[:offset] else 0
        minute=int(time[offset:]) if time[offset:] else 0

        start_time=datetime(year=dt.year, month=dt.month, day=dt.day, hour=hour, minute=minute)
        start_time-=timedelta(seconds=1)
        first_item=Item.objects.filter(Q(start_time__gte=start_time)).first()
        if orderby.upper() == "ASC":
            end_time=first_item.start_time+timedelta(hours=4)

            items=Item.objects.filter(Q(start_time__gte=start_time), Q(start_time__lte=end_time))
        else:
            end_time=start_time
            start_time=first_item.start_time-timedelta(hours=4)

            items=Item.objects.filter(Q(start_time__gte=start_time), Q(start_time__lte=end_time))

        if mall.upper() != "ALL":
            items=items.filter(mall__name=mall)
        
        if category.upper() != "ALL":
            items=items.filter(category__name=category)

        items=items.values(
            'name', 'mall__name', 'mall__label', 'category__name',
            'start_time', 'end_time', 'img', 'url', 'price', 'org_price',
        )
        return JsonResponse({'items':list(items)})