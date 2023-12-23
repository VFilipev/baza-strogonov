#! -*- coding=utf-8 -*-
from django.shortcuts import render
from lodge.models import Lodge, UslugiGroup, Photos, Price, Special_price
from order.models import Order_lodge
from . serializers import LodgeSerializer, PriceSerializer, SpecialPriceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from rest_framework import viewsets
from rest_framework.decorators import action
import datetime
from rest_framework.response import Response

class LodgeSetFilter(FilterSet):
    class Meta:
        model = Lodge
        fields = ['name', 'avalible']

class LodgeViewSet(viewsets.ModelViewSet):
    queryset = Lodge.objects.all()
    model = Lodge
    serializer_class = LodgeSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class  = LodgeSetFilter

    @action(detail=False,methods=['GET'])
    def get_free_lodge(self,request):
        ds = request.GET.get('date_start', '')
        de = request.GET.get('date_end', '')
        firstDay = datetime.datetime.strptime(ds, '%d.%m.%Y')
        lastDate = datetime.datetime.strptime(de, '%d.%m.%Y')                
        queryset = self.model.objects.all().filter(avalible=True)
        lodge_list = []
        order_list = Order_lodge.objects.all()
        availList = []            
        for l in queryset:
            order_list_for_l = order_list.filter(lodge=l.id)
            for o in order_list_for_l:                
                if o.start_date > lastDate.date() or o.end_date < firstDay.date():
                    availList.append(True)
                else:
                    availList.append(False)
            if all(availList):
                # p = Price.objects.filter(lodge=l.id).values('days', 'cost')
                # tmp = {}
                # for k in p:
                #     for d in k['days']:
                #         if d.isdigit():
                #             tmp[d] = k['cost'] 
                serializer = self.get_serializer(l)
                serializer_lodge = serializer.data
                # return (Response(serializer.data))                
                # price_set = Special_price.objects.filter(lodge=l.id).values('name','cost')                
                # photo_gallery_set = Photos.objects.filter(lodge=l.id).values('img','name')                
                lodge_list.append(
                    serializer_lodge
                    ) 
            availList = []    
        return Response(lodge_list)
    
class PriceSetFilter(FilterSet):
    class Meta:
        model = Price
        fields = ['lodge']

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    model = Price
    serializer_class = PriceSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class  = PriceSetFilter
    
class SpecialPriceSetFilter(FilterSet):
    class Meta:
        model = Special_price
        fields = ['lodge', 'active']

class SpecialPriceViewSet(viewsets.ModelViewSet):
    queryset = Special_price.objects.all()
    model = Special_price
    serializer_class = SpecialPriceSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class  = SpecialPriceSetFilter

